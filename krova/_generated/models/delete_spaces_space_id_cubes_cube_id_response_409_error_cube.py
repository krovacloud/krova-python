from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCube")


@_attrs_define
class DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCube:
    """
    Attributes:
        id (str | Unset):
        termination_protection_changed_at (datetime.datetime | None | Unset):
        termination_protection_changed_by (None | str | Unset):
    """

    id: str | Unset = UNSET
    termination_protection_changed_at: datetime.datetime | None | Unset = UNSET
    termination_protection_changed_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        termination_protection_changed_at: None | str | Unset
        if isinstance(self.termination_protection_changed_at, Unset):
            termination_protection_changed_at = UNSET
        elif isinstance(self.termination_protection_changed_at, datetime.datetime):
            termination_protection_changed_at = (
                self.termination_protection_changed_at.isoformat()
            )
        else:
            termination_protection_changed_at = self.termination_protection_changed_at

        termination_protection_changed_by: None | str | Unset
        if isinstance(self.termination_protection_changed_by, Unset):
            termination_protection_changed_by = UNSET
        else:
            termination_protection_changed_by = self.termination_protection_changed_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if termination_protection_changed_at is not UNSET:
            field_dict["terminationProtectionChangedAt"] = (
                termination_protection_changed_at
            )
        if termination_protection_changed_by is not UNSET:
            field_dict["terminationProtectionChangedBy"] = (
                termination_protection_changed_by
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_termination_protection_changed_at(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_protection_changed_at_type_0 = isoparse(data)

                return termination_protection_changed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        termination_protection_changed_at = _parse_termination_protection_changed_at(
            d.pop("terminationProtectionChangedAt", UNSET)
        )

        def _parse_termination_protection_changed_by(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        termination_protection_changed_by = _parse_termination_protection_changed_by(
            d.pop("terminationProtectionChangedBy", UNSET)
        )

        delete_spaces_space_id_cubes_cube_id_response_409_error_cube = cls(
            id=id,
            termination_protection_changed_at=termination_protection_changed_at,
            termination_protection_changed_by=termination_protection_changed_by,
        )

        delete_spaces_space_id_cubes_cube_id_response_409_error_cube.additional_properties = d
        return delete_spaces_space_id_cubes_cube_id_response_409_error_cube

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
