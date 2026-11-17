from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0")


@_attrs_define
class PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0:
    """
    Attributes:
        vcpus (int | Unset):
        ram_mb (int | Unset):
        disk_limit_gb (int | Unset):
    """

    vcpus: int | Unset = UNSET
    ram_mb: int | Unset = UNSET
    disk_limit_gb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vcpus = self.vcpus

        ram_mb = self.ram_mb

        disk_limit_gb = self.disk_limit_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vcpus is not UNSET:
            field_dict["vcpus"] = vcpus
        if ram_mb is not UNSET:
            field_dict["ramMb"] = ram_mb
        if disk_limit_gb is not UNSET:
            field_dict["diskLimitGb"] = disk_limit_gb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vcpus = d.pop("vcpus", UNSET)

        ram_mb = d.pop("ramMb", UNSET)

        disk_limit_gb = d.pop("diskLimitGb", UNSET)

        post_spaces_space_id_cubes_imports_body_expected_config_type_0 = cls(
            vcpus=vcpus,
            ram_mb=ram_mb,
            disk_limit_gb=disk_limit_gb,
        )

        post_spaces_space_id_cubes_imports_body_expected_config_type_0.additional_properties = d
        return post_spaces_space_id_cubes_imports_body_expected_config_type_0

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
