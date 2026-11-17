from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_spaces_space_id_cubes_imports_response_201_parts_item import (
        PostSpacesSpaceIdCubesImportsResponse201PartsItem,
    )


T = TypeVar("T", bound="PostSpacesSpaceIdCubesImportsResponse201")


@_attrs_define
class PostSpacesSpaceIdCubesImportsResponse201:
    """
    Attributes:
        import_id (str | Unset):
        upload_id (str | Unset):
        key (str | Unset):
        chunk_size_bytes (int | Unset):
        parts (list[PostSpacesSpaceIdCubesImportsResponse201PartsItem] | Unset):
        expires_at (datetime.datetime | Unset):
    """

    import_id: str | Unset = UNSET
    upload_id: str | Unset = UNSET
    key: str | Unset = UNSET
    chunk_size_bytes: int | Unset = UNSET
    parts: list[PostSpacesSpaceIdCubesImportsResponse201PartsItem] | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_id = self.import_id

        upload_id = self.upload_id

        key = self.key

        chunk_size_bytes = self.chunk_size_bytes

        parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_id is not UNSET:
            field_dict["importId"] = import_id
        if upload_id is not UNSET:
            field_dict["uploadId"] = upload_id
        if key is not UNSET:
            field_dict["key"] = key
        if chunk_size_bytes is not UNSET:
            field_dict["chunkSizeBytes"] = chunk_size_bytes
        if parts is not UNSET:
            field_dict["parts"] = parts
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_spaces_space_id_cubes_imports_response_201_parts_item import (
            PostSpacesSpaceIdCubesImportsResponse201PartsItem,
        )

        d = dict(src_dict)
        import_id = d.pop("importId", UNSET)

        upload_id = d.pop("uploadId", UNSET)

        key = d.pop("key", UNSET)

        chunk_size_bytes = d.pop("chunkSizeBytes", UNSET)

        _parts = d.pop("parts", UNSET)
        parts: list[PostSpacesSpaceIdCubesImportsResponse201PartsItem] | Unset = UNSET
        if _parts is not UNSET:
            parts = []
            for parts_item_data in _parts:
                parts_item = (
                    PostSpacesSpaceIdCubesImportsResponse201PartsItem.from_dict(
                        parts_item_data
                    )
                )

                parts.append(parts_item)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        post_spaces_space_id_cubes_imports_response_201 = cls(
            import_id=import_id,
            upload_id=upload_id,
            key=key,
            chunk_size_bytes=chunk_size_bytes,
            parts=parts,
            expires_at=expires_at,
        )

        post_spaces_space_id_cubes_imports_response_201.additional_properties = d
        return post_spaces_space_id_cubes_imports_response_201

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
