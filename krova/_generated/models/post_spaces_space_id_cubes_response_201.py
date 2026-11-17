from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cube import Cube


T = TypeVar("T", bound="PostSpacesSpaceIdCubesResponse201")


@_attrs_define
class PostSpacesSpaceIdCubesResponse201:
    """
    Attributes:
        cube (Cube | Unset):
    """

    cube: Cube | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cube: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cube, Unset):
            cube = self.cube.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cube is not UNSET:
            field_dict["cube"] = cube

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cube import Cube

        d = dict(src_dict)
        _cube = d.pop("cube", UNSET)
        cube: Cube | Unset
        if isinstance(_cube, Unset):
            cube = UNSET
        else:
            cube = Cube.from_dict(_cube)

        post_spaces_space_id_cubes_response_201 = cls(
            cube=cube,
        )

        post_spaces_space_id_cubes_response_201.additional_properties = d
        return post_spaces_space_id_cubes_response_201

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
