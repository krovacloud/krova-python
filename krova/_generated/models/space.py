from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.space_api_key_type_0 import SpaceApiKeyType0


T = TypeVar("T", bound="Space")


@_attrs_define
class Space:
    """
    Attributes:
        id (str):
        name (str):
        tier (str):
        created_at (datetime.datetime):
        api_key (None | SpaceApiKeyType0 | Unset): The API key this request authenticated with, or null when an OAuth
            access token did.
    """

    id: str
    name: str
    tier: str
    created_at: datetime.datetime
    api_key: None | SpaceApiKeyType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.space_api_key_type_0 import SpaceApiKeyType0

        id = self.id

        name = self.name

        tier = self.tier

        created_at = self.created_at.isoformat()

        api_key: dict[str, Any] | None | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        elif isinstance(self.api_key, SpaceApiKeyType0):
            api_key = self.api_key.to_dict()
        else:
            api_key = self.api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "tier": tier,
                "createdAt": created_at,
            }
        )
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.space_api_key_type_0 import SpaceApiKeyType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        tier = d.pop("tier")

        created_at = isoparse(d.pop("createdAt"))

        def _parse_api_key(data: object) -> None | SpaceApiKeyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_key_type_0 = SpaceApiKeyType0.from_dict(data)

                return api_key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpaceApiKeyType0 | Unset, data)

        api_key = _parse_api_key(d.pop("apiKey", UNSET))

        space = cls(
            id=id,
            name=name,
            tier=tier,
            created_at=created_at,
            api_key=api_key,
        )

        space.additional_properties = d
        return space

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
