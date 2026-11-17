from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchSpacesSpaceIdCubesCubeIdBody")


@_attrs_define
class PatchSpacesSpaceIdCubesCubeIdBody:
    """
    Attributes:
        name (str | Unset): New display name. 1–64 printable characters after trimming, the same rule as Cube creation.
        termination_protection (bool | Unset): Turn protection on or off. Turning it on stamps
            `terminationProtectionChangedAt` and `terminationProtectionChangedBy`; turning it off clears both.
        idle_timeout_minutes (int | None | Unset): Minutes without activity after which Krova powers the Cube off. Null
            (the default) turns this off. A Cube counts as idle when no web terminal or SSH session is open and its CPU
            stays under 5% busy with a 5-minute load average under 0.1. Termination protection does not stop this power-off.
            Send null to turn it off; anything other than an integer from 10 to 10080 (7 days) or null is rejected with 400.
    """

    name: str | Unset = UNSET
    termination_protection: bool | Unset = UNSET
    idle_timeout_minutes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        termination_protection = self.termination_protection

        idle_timeout_minutes: int | None | Unset
        if isinstance(self.idle_timeout_minutes, Unset):
            idle_timeout_minutes = UNSET
        else:
            idle_timeout_minutes = self.idle_timeout_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if termination_protection is not UNSET:
            field_dict["terminationProtection"] = termination_protection
        if idle_timeout_minutes is not UNSET:
            field_dict["idleTimeoutMinutes"] = idle_timeout_minutes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        termination_protection = d.pop("terminationProtection", UNSET)

        def _parse_idle_timeout_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idle_timeout_minutes = _parse_idle_timeout_minutes(
            d.pop("idleTimeoutMinutes", UNSET)
        )

        patch_spaces_space_id_cubes_cube_id_body = cls(
            name=name,
            termination_protection=termination_protection,
            idle_timeout_minutes=idle_timeout_minutes,
        )

        patch_spaces_space_id_cubes_cube_id_body.additional_properties = d
        return patch_spaces_space_id_cubes_cube_id_body

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
