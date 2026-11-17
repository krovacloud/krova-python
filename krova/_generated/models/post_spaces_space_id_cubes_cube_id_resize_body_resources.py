from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpacesSpaceIdCubesCubeIdResizeBodyResources")


@_attrs_define
class PostSpacesSpaceIdCubesCubeIdResizeBodyResources:
    """
    Attributes:
        vcpu (int | Unset):
        ram_gb (float | Unset): RAM in GB (1 = 1 GB), the same unit as Cube creation.
        disk_gb (int | Unset): Disk in GB. Grow-only.
    """

    vcpu: int | Unset = UNSET
    ram_gb: float | Unset = UNSET
    disk_gb: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        vcpu = self.vcpu

        ram_gb = self.ram_gb

        disk_gb = self.disk_gb

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if vcpu is not UNSET:
            field_dict["vcpu"] = vcpu
        if ram_gb is not UNSET:
            field_dict["ramGb"] = ram_gb
        if disk_gb is not UNSET:
            field_dict["diskGb"] = disk_gb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vcpu = d.pop("vcpu", UNSET)

        ram_gb = d.pop("ramGb", UNSET)

        disk_gb = d.pop("diskGb", UNSET)

        post_spaces_space_id_cubes_cube_id_resize_body_resources = cls(
            vcpu=vcpu,
            ram_gb=ram_gb,
            disk_gb=disk_gb,
        )

        return post_spaces_space_id_cubes_cube_id_resize_body_resources
