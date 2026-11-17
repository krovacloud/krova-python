from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Snapshot")


@_attrs_define
class Snapshot:
    """
    Attributes:
        id (str):
        cube_id (str):
        name (str):
        size_bytes (int | None):
        status (str):
        kind (str):
        created_at (datetime.datetime):
    """

    id: str
    cube_id: str
    name: str
    size_bytes: int | None
    status: str
    kind: str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        cube_id = self.cube_id

        name = self.name

        size_bytes: int | None
        size_bytes = self.size_bytes

        status = self.status

        kind = self.kind

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "cubeId": cube_id,
                "name": name,
                "sizeBytes": size_bytes,
                "status": status,
                "kind": kind,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        cube_id = d.pop("cubeId")

        name = d.pop("name")

        def _parse_size_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        size_bytes = _parse_size_bytes(d.pop("sizeBytes"))

        status = d.pop("status")

        kind = d.pop("kind")

        created_at = isoparse(d.pop("createdAt"))

        snapshot = cls(
            id=id,
            cube_id=cube_id,
            name=name,
            size_bytes=size_bytes,
            status=status,
            kind=kind,
            created_at=created_at,
        )

        snapshot.additional_properties = d
        return snapshot

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
