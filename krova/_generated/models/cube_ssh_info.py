from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cube_ssh_info_host_keys_item import CubeSshInfoHostKeysItem


T = TypeVar("T", bound="CubeSshInfo")


@_attrs_define
class CubeSshInfo:
    """
    Attributes:
        host (None | str):
        port (int):
        user (str):
        host_keys (list[CubeSshInfoHostKeysItem]):
    """

    host: None | str
    port: int
    user: str
    host_keys: list[CubeSshInfoHostKeysItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host: None | str
        host = self.host

        port = self.port

        user = self.user

        host_keys = []
        for host_keys_item_data in self.host_keys:
            host_keys_item = host_keys_item_data.to_dict()
            host_keys.append(host_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "port": port,
                "user": user,
                "hostKeys": host_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cube_ssh_info_host_keys_item import CubeSshInfoHostKeysItem

        d = dict(src_dict)

        def _parse_host(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        host = _parse_host(d.pop("host"))

        port = d.pop("port")

        user = d.pop("user")

        host_keys = []
        _host_keys = d.pop("hostKeys")
        for host_keys_item_data in _host_keys:
            host_keys_item = CubeSshInfoHostKeysItem.from_dict(host_keys_item_data)

            host_keys.append(host_keys_item)

        cube_ssh_info = cls(
            host=host,
            port=port,
            user=user,
            host_keys=host_keys,
        )

        cube_ssh_info.additional_properties = d
        return cube_ssh_info

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
