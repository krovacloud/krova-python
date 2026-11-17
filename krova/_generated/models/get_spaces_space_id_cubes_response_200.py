from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cube import Cube
    from ..models.pagination import Pagination


T = TypeVar("T", bound="GetSpacesSpaceIdCubesResponse200")


@_attrs_define
class GetSpacesSpaceIdCubesResponse200:
    """
    Attributes:
        cubes (list[Cube]):
        pagination (Pagination):
    """

    cubes: list[Cube]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cubes = []
        for cubes_item_data in self.cubes:
            cubes_item = cubes_item_data.to_dict()
            cubes.append(cubes_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cubes": cubes,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cube import Cube
        from ..models.pagination import Pagination

        d = dict(src_dict)
        cubes = []
        _cubes = d.pop("cubes")
        for cubes_item_data in _cubes:
            cubes_item = Cube.from_dict(cubes_item_data)

            cubes.append(cubes_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        get_spaces_space_id_cubes_response_200 = cls(
            cubes=cubes,
            pagination=pagination,
        )

        get_spaces_space_id_cubes_response_200.additional_properties = d
        return get_spaces_space_id_cubes_response_200

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
