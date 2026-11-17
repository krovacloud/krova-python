from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_spaces_space_id_cubes_imports_import_id_complete_body_config import (
        PostSpacesSpaceIdCubesImportsImportIdCompleteBodyConfig,
    )
    from ..models.post_spaces_space_id_cubes_imports_import_id_complete_body_parts_item import (
        PostSpacesSpaceIdCubesImportsImportIdCompleteBodyPartsItem,
    )


T = TypeVar("T", bound="PostSpacesSpaceIdCubesImportsImportIdCompleteBody")


@_attrs_define
class PostSpacesSpaceIdCubesImportsImportIdCompleteBody:
    """
    Attributes:
        parts (list[PostSpacesSpaceIdCubesImportsImportIdCompleteBodyPartsItem]):
        config (PostSpacesSpaceIdCubesImportsImportIdCompleteBodyConfig):
    """

    parts: list[PostSpacesSpaceIdCubesImportsImportIdCompleteBodyPartsItem]
    config: PostSpacesSpaceIdCubesImportsImportIdCompleteBodyConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parts = []
        for parts_item_data in self.parts:
            parts_item = parts_item_data.to_dict()
            parts.append(parts_item)

        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parts": parts,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_spaces_space_id_cubes_imports_import_id_complete_body_config import (
            PostSpacesSpaceIdCubesImportsImportIdCompleteBodyConfig,
        )
        from ..models.post_spaces_space_id_cubes_imports_import_id_complete_body_parts_item import (
            PostSpacesSpaceIdCubesImportsImportIdCompleteBodyPartsItem,
        )

        d = dict(src_dict)
        parts = []
        _parts = d.pop("parts")
        for parts_item_data in _parts:
            parts_item = (
                PostSpacesSpaceIdCubesImportsImportIdCompleteBodyPartsItem.from_dict(
                    parts_item_data
                )
            )

            parts.append(parts_item)

        config = PostSpacesSpaceIdCubesImportsImportIdCompleteBodyConfig.from_dict(
            d.pop("config")
        )

        post_spaces_space_id_cubes_imports_import_id_complete_body = cls(
            parts=parts,
            config=config,
        )

        post_spaces_space_id_cubes_imports_import_id_complete_body.additional_properties = d
        return post_spaces_space_id_cubes_imports_import_id_complete_body

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
