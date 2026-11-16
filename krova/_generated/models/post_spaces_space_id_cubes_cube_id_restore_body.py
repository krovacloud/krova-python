from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSpacesSpaceIdCubesCubeIdRestoreBody")


@_attrs_define
class PostSpacesSpaceIdCubesCubeIdRestoreBody:
    """
    Attributes:
        snapshot_id (str):
    """

    snapshot_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshotId": snapshot_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        snapshot_id = d.pop("snapshotId")

        post_spaces_space_id_cubes_cube_id_restore_body = cls(
            snapshot_id=snapshot_id,
        )

        post_spaces_space_id_cubes_cube_id_restore_body.additional_properties = d
        return post_spaces_space_id_cubes_cube_id_restore_body

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
