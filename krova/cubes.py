"""Cubes: create, read, list, delete, power off, SSH info, and wait until running.

Running commands and moving files (``run()`` and ``files``) are not here yet. They will attach
to the ``Cube`` handle below as separate modules, so nothing in this file needs to change.
"""

from __future__ import annotations

import time
from dataclasses import dataclass

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
    post_spaces_space_id_cubes as _create_cube,
)
from ._generated.api.cubes import (
    post_spaces_space_id_cubes_cube_id_power_off as _power_off,
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
from ._generated.models.post_spaces_space_id_cubes_body import PostSpacesSpaceIdCubesBody
from ._generated.models.post_spaces_space_id_cubes_body_resources import (
    PostSpacesSpaceIdCubesBodyResources,
)
from ._generated.models.post_spaces_space_id_cubes_response_201 import (
    PostSpacesSpaceIdCubesResponse201,
)
from ._generated.types import UNSET
from ._http import Transport
from .errors import CubeFailedError, KrovaError, WaitTimeoutError

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

    def refresh(self) -> Cube:
        """Reload this Cube from the API and return it."""
        self.data = self._cubes.get(self.id).data
        return self

    def ssh(self) -> SshInfo:
        return self._cubes.ssh(self.id)

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
        idempotency_key: str | None = None,
    ) -> Cube:
        """Create a Cube. It starts out ``pending``; use ``cube.wait_until_running()``.

        ``ssh_public_key`` is written to the Cube's login user at boot. ``region`` is a slug from
        the regions catalog. ``user_data`` is a cloud-init script (16 KB at most). An
        ``idempotency_key`` makes a retried create return the original Cube.
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

    def delete(self, cube_id: str) -> None:
        """Queue the Cube for deletion. A Cube with termination protection raises
        ``KrovaError`` with status 409 and code ``termination_protected``."""
        self._transport.call(_delete_cube, self._space_id, cube_id)

    def power_off(self, cube_id: str) -> None:
        self._transport.call(_power_off, self._space_id, cube_id)

    def ssh(self, cube_id: str) -> SshInfo:
        response = self._transport.call(_get_ssh, self._space_id, cube_id)
        return SshInfo._from_generated(CubeSshInfo.from_dict(response.json()))
