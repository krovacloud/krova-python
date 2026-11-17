from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200Summary"
)


@_attrs_define
class GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200Summary:
    """
    Attributes:
        found (int):
        total (int):
        complete (bool):
    """

    found: int
    total: int
    complete: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        found = self.found

        total = self.total

        complete = self.complete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "found": found,
                "total": total,
                "complete": complete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        found = d.pop("found")

        total = d.pop("total")

        complete = d.pop("complete")

        get_spaces_space_id_cubes_cube_id_domains_mapping_id_records_response_200_summary = cls(
            found=found,
            total=total,
            complete=complete,
        )

        get_spaces_space_id_cubes_cube_id_domains_mapping_id_records_response_200_summary.additional_properties = d
        return get_spaces_space_id_cubes_cube_id_domains_mapping_id_records_response_200_summary

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
