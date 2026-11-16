from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSpacesSpaceIdCubesBodyResources")


@_attrs_define
class PostSpacesSpaceIdCubesBodyResources:
    """
    Attributes:
        vcpu (float):
        ram_gb (float):
        disk_gb (float):
    """

    vcpu: float
    ram_gb: float
    disk_gb: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vcpu = self.vcpu

        ram_gb = self.ram_gb

        disk_gb = self.disk_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vcpu": vcpu,
                "ramGb": ram_gb,
                "diskGb": disk_gb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vcpu = d.pop("vcpu")

        ram_gb = d.pop("ramGb")

        disk_gb = d.pop("diskGb")

        post_spaces_space_id_cubes_body_resources = cls(
            vcpu=vcpu,
            ram_gb=ram_gb,
            disk_gb=disk_gb,
        )

        post_spaces_space_id_cubes_body_resources.additional_properties = d
        return post_spaces_space_id_cubes_body_resources

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
