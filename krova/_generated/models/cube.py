from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cube_state import CubeState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cube_resources import CubeResources


T = TypeVar("T", bound="Cube")


@_attrs_define
class Cube:
    """
    Attributes:
        id (str):
        name (str):
        state (CubeState):
        public_ipv_4 (None | str):
        resources (CubeResources):
        image (str):
        ssh_user (str):
        cost_per_hour (float):
        termination_protection (bool): Per-cube opt-in flag. When true, customer-initiated destroy paths return 409 with
            `error.code = "termination_protected"`. Power-off, wake, restart, restore, network-reset, and snapshot ops are
            NOT termination and remain allowed. Default false.
        termination_protection_changed_at (datetime.datetime | None): ISO8601 timestamp of the most recent toggle of
            `terminationProtection`. Null when the flag has never been turned on.
        termination_protection_changed_by (None | str): Identifies the actor that last toggled the flag: `"user:<id>"`
            for a customer, `"admin:<id>"` for an operator, `"system:<job-name>"` for a worker-driven write. Null when the
            flag has never been turned on.
        idle_timeout_minutes (int | None): Minutes without activity after which Krova powers the Cube off. Null (the
            default) turns this off. A Cube counts as idle when no web terminal or SSH session is open and its CPU stays
            under 5% busy with a 5-minute load average under 0.1. Termination protection does not stop this power-off.
        last_active_at (datetime.datetime | None): ISO8601 timestamp of the last time Krova saw the Cube active (a web
            terminal or SSH session open, or CPU at or above 5% busy, or a 5-minute load average at or above 0.1). Null
            until the idle check has recorded one.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        server_domain (None | str | Unset): The hostname of the server currently hosting this Cube (e.g.
            `mango.krova.cloud`), shared by every Cube on that server. This is NOT the Cube's own SSH target — use `host`
            from GET .../ssh for that, which is the Cube's own stable hostname and survives migration to another server.
            Null when the Cube has no server assigned. Only present on the single-Cube GET; list and create responses omit
            it.
    """

    id: str
    name: str
    state: CubeState
    public_ipv_4: None | str
    resources: CubeResources
    image: str
    ssh_user: str
    cost_per_hour: float
    termination_protection: bool
    termination_protection_changed_at: datetime.datetime | None
    termination_protection_changed_by: None | str
    idle_timeout_minutes: int | None
    last_active_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    server_domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        state = self.state.value

        public_ipv_4: None | str
        public_ipv_4 = self.public_ipv_4

        resources = self.resources.to_dict()

        image = self.image

        ssh_user = self.ssh_user

        cost_per_hour = self.cost_per_hour

        termination_protection = self.termination_protection

        termination_protection_changed_at: None | str
        if isinstance(self.termination_protection_changed_at, datetime.datetime):
            termination_protection_changed_at = (
                self.termination_protection_changed_at.isoformat()
            )
        else:
            termination_protection_changed_at = self.termination_protection_changed_at

        termination_protection_changed_by: None | str
        termination_protection_changed_by = self.termination_protection_changed_by

        idle_timeout_minutes: int | None
        idle_timeout_minutes = self.idle_timeout_minutes

        last_active_at: None | str
        if isinstance(self.last_active_at, datetime.datetime):
            last_active_at = self.last_active_at.isoformat()
        else:
            last_active_at = self.last_active_at

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        server_domain: None | str | Unset
        if isinstance(self.server_domain, Unset):
            server_domain = UNSET
        else:
            server_domain = self.server_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "publicIpv4": public_ipv_4,
                "resources": resources,
                "image": image,
                "sshUser": ssh_user,
                "costPerHour": cost_per_hour,
                "terminationProtection": termination_protection,
                "terminationProtectionChangedAt": termination_protection_changed_at,
                "terminationProtectionChangedBy": termination_protection_changed_by,
                "idleTimeoutMinutes": idle_timeout_minutes,
                "lastActiveAt": last_active_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if server_domain is not UNSET:
            field_dict["serverDomain"] = server_domain

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cube_resources import CubeResources

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        state = CubeState(d.pop("state"))

        def _parse_public_ipv_4(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        public_ipv_4 = _parse_public_ipv_4(d.pop("publicIpv4"))

        resources = CubeResources.from_dict(d.pop("resources"))

        image = d.pop("image")

        ssh_user = d.pop("sshUser")

        cost_per_hour = d.pop("costPerHour")

        termination_protection = d.pop("terminationProtection")

        def _parse_termination_protection_changed_at(
            data: object,
        ) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_protection_changed_at_type_0 = isoparse(data)

                return termination_protection_changed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        termination_protection_changed_at = _parse_termination_protection_changed_at(
            d.pop("terminationProtectionChangedAt")
        )

        def _parse_termination_protection_changed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        termination_protection_changed_by = _parse_termination_protection_changed_by(
            d.pop("terminationProtectionChangedBy")
        )

        def _parse_idle_timeout_minutes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        idle_timeout_minutes = _parse_idle_timeout_minutes(d.pop("idleTimeoutMinutes"))

        def _parse_last_active_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_active_at_type_0 = isoparse(data)

                return last_active_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_active_at = _parse_last_active_at(d.pop("lastActiveAt"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_server_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_domain = _parse_server_domain(d.pop("serverDomain", UNSET))

        cube = cls(
            id=id,
            name=name,
            state=state,
            public_ipv_4=public_ipv_4,
            resources=resources,
            image=image,
            ssh_user=ssh_user,
            cost_per_hour=cost_per_hour,
            termination_protection=termination_protection,
            termination_protection_changed_at=termination_protection_changed_at,
            termination_protection_changed_by=termination_protection_changed_by,
            idle_timeout_minutes=idle_timeout_minutes,
            last_active_at=last_active_at,
            created_at=created_at,
            updated_at=updated_at,
            server_domain=server_domain,
        )

        cube.additional_properties = d
        return cube

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
