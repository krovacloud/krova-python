"""Cubes: create, read, list, rename, resize, idle auto-stop, delete, power off, SSH info, connect.

Running commands and moving files live in ``shell.py``; ``connect`` here opens that connection.
"""

from __future__ import annotations

import datetime
import time
from collections.abc import Sequence
from dataclasses import dataclass

import paramiko

from ._generated.api.cubes import (
    delete_spaces_space_id_cubes_cube_id as _delete_cube,
)
from ._generated.api.cubes import (
    get_spaces_space_id_cubes as _list_cubes,
)
from ._generated.api.cubes import (
    get_spaces_space_id_cubes_cube_id as _get_cube,
)
from ._generated.api.cubes import (
    get_spaces_space_id_cubes_cube_id_ssh as _get_ssh,
)
from ._generated.api.cubes import (
    patch_spaces_space_id_cubes_cube_id as _update_cube,
)
from ._generated.api.cubes import (
    post_spaces_space_id_cubes as _create_cube,
)
from ._generated.api.cubes import (
    post_spaces_space_id_cubes_cube_id_power_off as _power_off,
)
from ._generated.api.cubes import (
    post_spaces_space_id_cubes_cube_id_resize as _resize_cube,
)
from ._generated.models.cube import Cube as CubeData
from ._generated.models.cube_ssh_info import CubeSshInfo
from ._generated.models.cube_state import CubeState
from ._generated.models.get_spaces_space_id_cubes_cube_id_response_200 import (
    GetSpacesSpaceIdCubesCubeIdResponse200,
)
from ._generated.models.get_spaces_space_id_cubes_response_200 import (
    GetSpacesSpaceIdCubesResponse200,
)
from ._generated.models.patch_spaces_space_id_cubes_cube_id_body import (
    PatchSpacesSpaceIdCubesCubeIdBody,
)
from ._generated.models.patch_spaces_space_id_cubes_cube_id_response_200 import (
    PatchSpacesSpaceIdCubesCubeIdResponse200,
)
from ._generated.models.post_spaces_space_id_cubes_body import PostSpacesSpaceIdCubesBody
from ._generated.models.post_spaces_space_id_cubes_body_resources import (
    PostSpacesSpaceIdCubesBodyResources,
)
from ._generated.models.post_spaces_space_id_cubes_cube_id_resize_body import (
    PostSpacesSpaceIdCubesCubeIdResizeBody,
)
from ._generated.models.post_spaces_space_id_cubes_cube_id_resize_body_resources import (
    PostSpacesSpaceIdCubesCubeIdResizeBodyResources,
)
from ._generated.models.post_spaces_space_id_cubes_cube_id_resize_response_200 import (
    PostSpacesSpaceIdCubesCubeIdResizeResponse200,
)
from ._generated.models.post_spaces_space_id_cubes_response_201 import (
    PostSpacesSpaceIdCubesResponse201,
)
from ._generated.types import UNSET
from ._http import Transport
from .errors import CubeFailedError, KrovaError, WaitTimeoutError
from .shell import CubeShell, open_shell

# States a Cube cannot leave without you doing something, so waiting for "running" is pointless.
_DEAD_STATES = frozenset(
    {CubeState.ERROR, CubeState.DELETED, CubeState.STOPPED, CubeState.STOPPING}
)


@dataclass(frozen=True)
class HostKey:
    """One SSH host key of a Cube; pin it instead of trusting the first connection."""

    type: str
    key: str


@dataclass(frozen=True)
class SshInfo:
    """Where and how to connect to a Cube over SSH."""

    host: str | None
    port: int
    user: str
    host_keys: list[HostKey]

    @classmethod
    def _from_generated(cls, info: CubeSshInfo) -> SshInfo:
        return cls(
            host=info.host,
            port=info.port,
            user=info.user,
            host_keys=[HostKey(type=k.type_, key=k.key) for k in info.host_keys],
        )


@dataclass(frozen=True)
class CubeSize:
    """A Cube's vCPU count, RAM in GB and disk in GB."""

    vcpu: int
    ram_gb: float
    disk_gb: int


@dataclass(frozen=True)
class ResizeResult:
    """The answer to a resize request. The change itself is applied by a background job.

    The Cube keeps its current size until ``cube.refresh()`` shows the new one. ``is_live`` means
    the change applies with no restart; ``requires_restart`` is the inverse: the Cube is restarted
    to apply it.
    """

    job_id: str
    is_live: bool
    requires_restart: bool
    previous: CubeSize
    requested: CubeSize

    @classmethod
    def _from_generated(cls, data: PostSpacesSpaceIdCubesCubeIdResizeResponse200) -> ResizeResult:
        return cls(
            job_id=data.job_id,
            is_live=data.is_live,
            requires_restart=data.requires_restart,
            previous=CubeSize(data.previous.vcpu, data.previous.ram_gb, data.previous.disk_gb),
            requested=CubeSize(data.requested.vcpu, data.requested.ram_gb, data.requested.disk_gb),
        )


class Cube:
    """A Cube and the calls that act on it.

    Fields are a snapshot from the last API response; call ``refresh()`` for fresh ones.
    The full generated model is available as ``cube.data``.
    """

    def __init__(self, cubes: Cubes, data: CubeData) -> None:
        self._cubes = cubes
        self.data = data

    def __repr__(self) -> str:
        return f"Cube(id={self.id!r}, name={self.name!r}, state={self.state!r})"

    @property
    def id(self) -> str:
        return self.data.id

    @property
    def name(self) -> str:
        return self.data.name

    @property
    def state(self) -> str:
        """One of pending, booting, running, stopped, stopping, resizing, error, deleted."""
        return self.data.state.value

    @property
    def public_ipv4(self) -> str | None:
        return self.data.public_ipv_4

    @property
    def ssh_user(self) -> str:
        return self.data.ssh_user

    @property
    def idle_timeout_minutes(self) -> int | None:
        """Minutes without activity after which Krova powers the Cube off; ``None`` means off."""
        return self.data.idle_timeout_minutes

    @property
    def last_active_at(self) -> datetime.datetime | None:
        """The last time Krova saw the Cube active; ``None`` until the idle check records one."""
        return self.data.last_active_at

    def refresh(self) -> Cube:
        """Reload this Cube from the API and return it."""
        self.data = self._cubes.get(self.id).data
        return self

    def ssh(self) -> SshInfo:
        return self._cubes.ssh(self.id)

    def connect(
        self,
        *,
        private_key: str | bytes | paramiko.PKey,
        passphrase: str | None = None,
        timeout: float = 30.0,
        host_keys: Sequence[HostKey | str] | None = None,
    ) -> CubeShell:
        """Open an SSH connection to this Cube. See ``Cubes.connect``."""
        return self._cubes.connect(
            self.id,
            private_key=private_key,
            passphrase=passphrase,
            timeout=timeout,
            host_keys=host_keys,
        )

    def rename(self, name: str) -> Cube:
        """Rename this Cube and return it, updated. See ``Cubes.rename``."""
        self.data = self._cubes.rename(self.id, name).data
        return self

    def resize(
        self,
        *,
        vcpu: int | None = None,
        ram_gb: float | None = None,
        disk_gb: int | None = None,
        idempotency_key: str | None = None,
    ) -> ResizeResult:
        """Queue a resize of this Cube. See ``Cubes.resize``."""
        return self._cubes.resize(
            self.id,
            vcpu=vcpu,
            ram_gb=ram_gb,
            disk_gb=disk_gb,
            idempotency_key=idempotency_key,
        )

    def set_idle_timeout(self, minutes: int | None) -> Cube:
        """Set or clear the idle auto-stop timeout and return this Cube, updated."""
        self.data = self._cubes.set_idle_timeout(self.id, minutes).data
        return self

    def power_off(self) -> None:
        self._cubes.power_off(self.id)

    def delete(self) -> None:
        self._cubes.delete(self.id)

    def wait_until_running(
        self,
        timeout: float = 300.0,
        *,
        poll_interval: float = 1.0,
        max_interval: float = 10.0,
    ) -> Cube:
        """Poll until the Cube is ``running`` and return it.

        The wait between polls starts at ``poll_interval`` seconds and grows by half each time,
        up to ``max_interval``. Raises ``WaitTimeoutError`` after ``timeout`` seconds, and
        ``CubeFailedError`` if the Cube lands in ``error``, ``deleted``, ``stopped`` or
        ``stopping``, since it will not start running by itself from there.
        """
        deadline = time.monotonic() + timeout
        interval = poll_interval
        while True:
            self.refresh()
            if self.data.state is CubeState.RUNNING:
                return self
            if self.data.state in _DEAD_STATES:
                raise CubeFailedError(
                    f"Cube {self.id} is {self.state}, so it will not reach running",
                    cube_id=self.id,
                    state=self.state,
                )
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise WaitTimeoutError(
                    f"Cube {self.id} was still {self.state} after {timeout:g}s",
                    cube_id=self.id,
                    state=self.state,
                )
            time.sleep(min(interval, remaining))
            interval = min(interval * 1.5, max_interval)


class Cubes:
    """``client.cubes``: the Cube endpoints of one Space."""

    def __init__(self, transport: Transport, space_id: str) -> None:
        self._transport = transport
        self._space_id = space_id

    def create(
        self,
        *,
        name: str,
        image: str,
        vcpu: float,
        ram_gb: float,
        disk_gb: float,
        ssh_public_key: str,
        region: str | None = None,
        user_data: str | None = None,
        termination_protection: bool = False,
        idle_timeout_minutes: int | None = None,
        idempotency_key: str | None = None,
    ) -> Cube:
        """Create a Cube. It starts out ``pending``; use ``cube.wait_until_running()``.

        ``ssh_public_key`` is written to the Cube's login user at boot. ``region`` is a slug from
        the regions catalog. ``user_data`` is a cloud-init script (16 KB at most).
        ``idle_timeout_minutes`` powers the Cube off after that many idle minutes (10 to 10080);
        the disk is kept. Leave it out to keep auto-stop off. An ``idempotency_key`` makes a
        retried create return the original Cube.
        """
        body = PostSpacesSpaceIdCubesBody(
            name=name,
            image=image,
            resources=PostSpacesSpaceIdCubesBodyResources(
                vcpu=vcpu, ram_gb=ram_gb, disk_gb=disk_gb
            ),
            ssh_public_key=ssh_public_key,
            region=UNSET if region is None else region,
            user_data=UNSET if user_data is None else user_data,
            termination_protection=termination_protection,
            idle_timeout_minutes=UNSET if idle_timeout_minutes is None else idle_timeout_minutes,
        )
        response = self._transport.call(
            _create_cube,
            self._space_id,
            body=body,
            idempotency_key=UNSET if idempotency_key is None else idempotency_key,
        )
        parsed = PostSpacesSpaceIdCubesResponse201.from_dict(response.json())
        if parsed.cube is UNSET:
            raise KrovaError(
                "The API created the Cube but returned no cube",
                status=response.status_code,
                request_id=response.headers.get("x-request-id"),
            )
        return Cube(self, parsed.cube)

    def get(self, cube_id: str) -> Cube:
        response = self._transport.call(_get_cube, self._space_id, cube_id)
        parsed = GetSpacesSpaceIdCubesCubeIdResponse200.from_dict(response.json())
        return Cube(self, parsed.cube)

    def list(self) -> list[Cube]:
        response = self._transport.call(_list_cubes, self._space_id)
        parsed = GetSpacesSpaceIdCubesResponse200.from_dict(response.json())
        return [Cube(self, c) for c in parsed.cubes]

    def rename(self, cube_id: str, name: str) -> Cube:
        """Rename a Cube and return it, updated.

        The name is 1 to 64 printable characters and need not be unique in the Space. This is
        metadata only: the hostname inside a running Cube changes on its next cold restart.
        """
        return self._update(cube_id, PatchSpacesSpaceIdCubesCubeIdBody(name=name))

    def set_idle_timeout(self, cube_id: str, minutes: int | None) -> Cube:
        """Set the idle auto-stop timeout and return the Cube, updated.

        Krova powers the Cube off after ``minutes`` without activity (10 to 10080, the API
        rejects anything else); the disk is kept. Pass ``None`` to turn auto-stop off.
        """
        body = PatchSpacesSpaceIdCubesCubeIdBody(idle_timeout_minutes=minutes)
        return self._update(cube_id, body)

    def _update(self, cube_id: str, body: PatchSpacesSpaceIdCubesCubeIdBody) -> Cube:
        response = self._transport.call(_update_cube, self._space_id, cube_id, body=body)
        parsed = PatchSpacesSpaceIdCubesCubeIdResponse200.from_dict(response.json())
        return Cube(self, parsed.cube)

    def resize(
        self,
        cube_id: str,
        *,
        vcpu: int | None = None,
        ram_gb: float | None = None,
        disk_gb: int | None = None,
        idempotency_key: str | None = None,
    ) -> ResizeResult:
        """Queue a resize and return what was queued. Send only the sizes you want to change.

        A background job applies it, so the Cube keeps its current size until ``refresh()`` shows
        the new one. Disk can only grow. The Cube must be ``running`` or ``stopped``. The API
        answers 400 for an out-of-range size, a size above your plan's limit, a host without
        room or no change at all, and 409 while a resize is already queued.
        """
        body = PostSpacesSpaceIdCubesCubeIdResizeBody(
            resources=PostSpacesSpaceIdCubesCubeIdResizeBodyResources(
                vcpu=UNSET if vcpu is None else vcpu,
                ram_gb=UNSET if ram_gb is None else ram_gb,
                disk_gb=UNSET if disk_gb is None else disk_gb,
            )
        )
        response = self._transport.call(
            _resize_cube,
            self._space_id,
            cube_id,
            body=body,
            idempotency_key=UNSET if idempotency_key is None else idempotency_key,
        )
        return ResizeResult._from_generated(
            PostSpacesSpaceIdCubesCubeIdResizeResponse200.from_dict(response.json())
        )

    def delete(self, cube_id: str) -> None:
        """Queue the Cube for deletion. A Cube with termination protection raises
        ``KrovaError`` with status 409 and code ``termination_protected``."""
        self._transport.call(_delete_cube, self._space_id, cube_id)

    def power_off(self, cube_id: str) -> None:
        self._transport.call(_power_off, self._space_id, cube_id)

    def ssh(self, cube_id: str) -> SshInfo:
        response = self._transport.call(_get_ssh, self._space_id, cube_id)
        return SshInfo._from_generated(CubeSshInfo.from_dict(response.json()))

    def connect(
        self,
        cube_id: str,
        *,
        private_key: str | bytes | paramiko.PKey,
        passphrase: str | None = None,
        timeout: float = 30.0,
        host_keys: Sequence[HostKey | str] | None = None,
    ) -> CubeShell:
        """Open an SSH connection to a running Cube and return a ``CubeShell``.

        ``private_key`` is the private half of the key you passed as ``ssh_public_key`` when you
        created the Cube: an OpenSSH or PEM string (Ed25519, ECDSA or RSA) or a
        ``paramiko.PKey``. ``passphrase`` unlocks an encrypted key. Your SSH agent and
        ``~/.ssh`` are never consulted.

        The Cube's host keys come from ``cubes.ssh``. The server must present one of them, or
        ``HostKeyMismatchError`` is raised; so it is when the API has no keys for the Cube yet.
        ``host_keys`` replaces the keys from the API with ones you hold, as ``HostKey`` objects or
        ``"ssh-ed25519 AAAA..."`` lines. There is no way to turn the check off.
        """
        info = self.ssh(cube_id)
        if not info.host:
            raise KrovaError(f"Cube {cube_id} has no SSH address yet: wait until it is running")
        return open_shell(
            host=info.host,
            port=info.port,
            user=info.user,
            host_keys=info.host_keys if host_keys is None else host_keys,
            private_key=private_key,
            passphrase=passphrase,
            timeout=timeout,
        )
