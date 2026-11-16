from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_spaces_space_id_cubes_imports_import_id_complete_response_200_status import (
    PostSpacesSpaceIdCubesImportsImportIdCompleteResponse200Status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpacesSpaceIdCubesImportsImportIdCompleteResponse200")


@_attrs_define
class PostSpacesSpaceIdCubesImportsImportIdCompleteResponse200:
    """
    Attributes:
        import_id (str | Unset):
        cube_id (str | Unset):
        status (PostSpacesSpaceIdCubesImportsImportIdCompleteResponse200Status | Unset):
    """

    import_id: str | Unset = UNSET
    cube_id: str | Unset = UNSET
    status: PostSpacesSpaceIdCubesImportsImportIdCompleteResponse200Status | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_id = self.import_id

        cube_id = self.cube_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_id is not UNSET:
            field_dict["importId"] = import_id
        if cube_id is not UNSET:
            field_dict["cubeId"] = cube_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        import_id = d.pop("importId", UNSET)

        cube_id = d.pop("cubeId", UNSET)

        _status = d.pop("status", UNSET)
        status: PostSpacesSpaceIdCubesImportsImportIdCompleteResponse200Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PostSpacesSpaceIdCubesImportsImportIdCompleteResponse200Status(
                _status
            )

        post_spaces_space_id_cubes_imports_import_id_complete_response_200 = cls(
            import_id=import_id,
            cube_id=cube_id,
            status=status,
        )

        post_spaces_space_id_cubes_imports_import_id_complete_response_200.additional_properties = d
        return post_spaces_space_id_cubes_imports_import_id_complete_response_200

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
