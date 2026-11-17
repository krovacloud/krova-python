from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchSpacesSpaceIdCubesCubeIdBody")


@_attrs_define
class PatchSpacesSpaceIdCubesCubeIdBody:
    """
    Attributes:
        termination_protection (bool): Turn protection on or off. Turning it on stamps `terminationProtectionChangedAt`
            and `terminationProtectionChangedBy`; turning it off clears both.
    """

    termination_protection: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        termination_protection = self.termination_protection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "terminationProtection": termination_protection,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        termination_protection = d.pop("terminationProtection")

        patch_spaces_space_id_cubes_cube_id_body = cls(
            termination_protection=termination_protection,
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
