from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpacesSpaceIdCubesImportsResponse201PartsItem")


@_attrs_define
class PostSpacesSpaceIdCubesImportsResponse201PartsItem:
    """
    Attributes:
        part_number (int | Unset):
        url (str | Unset):
    """

    part_number: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        part_number = self.part_number

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        part_number = d.pop("partNumber", UNSET)

        url = d.pop("url", UNSET)

        post_spaces_space_id_cubes_imports_response_201_parts_item = cls(
            part_number=part_number,
            url=url,
        )

        post_spaces_space_id_cubes_imports_response_201_parts_item.additional_properties = d
        return post_spaces_space_id_cubes_imports_response_201_parts_item

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
