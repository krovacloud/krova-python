from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_spaces_space_id_cubes_imports_import_id_response_200_import_status import (
    GetSpacesSpaceIdCubesImportsImportIdResponse200ImportStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSpacesSpaceIdCubesImportsImportIdResponse200Import")


@_attrs_define
class GetSpacesSpaceIdCubesImportsImportIdResponse200Import:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        status (GetSpacesSpaceIdCubesImportsImportIdResponse200ImportStatus | Unset):
        cube_id (None | str | Unset):
        error (None | str | Unset):
        created_at (str | Unset):
        updated_at (str | Unset):
        completed_at (None | str | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: GetSpacesSpaceIdCubesImportsImportIdResponse200ImportStatus | Unset = UNSET
    cube_id: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        cube_id: None | str | Unset
        if isinstance(self.cube_id, Unset):
            cube_id = UNSET
        else:
            cube_id = self.cube_id

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        created_at = self.created_at

        updated_at = self.updated_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if cube_id is not UNSET:
            field_dict["cubeId"] = cube_id
        if error is not UNSET:
            field_dict["error"] = error
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: GetSpacesSpaceIdCubesImportsImportIdResponse200ImportStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetSpacesSpaceIdCubesImportsImportIdResponse200ImportStatus(
                _status
            )

        def _parse_cube_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cube_id = _parse_cube_id(d.pop("cubeId", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        def _parse_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        get_spaces_space_id_cubes_imports_import_id_response_200_import = cls(
            id=id,
            name=name,
            status=status,
            cube_id=cube_id,
            error=error,
            created_at=created_at,
            updated_at=updated_at,
            completed_at=completed_at,
        )

        get_spaces_space_id_cubes_imports_import_id_response_200_import.additional_properties = d
        return get_spaces_space_id_cubes_imports_import_id_response_200_import

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
