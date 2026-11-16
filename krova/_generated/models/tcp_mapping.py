from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tcp_mapping_whitelisted_ips_item import TcpMappingWhitelistedIpsItem


T = TypeVar("T", bound="TcpMapping")


@_attrs_define
class TcpMapping:
    """
    Attributes:
        id (str):
        cube_id (str):
        cube_port (int):
        host_port (int):
        label (None | str):
        status (str):
        is_ssh (bool):
        udp_enabled (bool): Whether this mapping also forwards UDP on the same host port. True means TCP and UDP; false
            means TCP only. Always false for the platform SSH mapping.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        whitelisted_ips (list[TcpMappingWhitelistedIpsItem]):
        host (None | str | Unset): Where to connect for this mapping: `host:hostPort`. The Cube's own stable hostname,
            which survives migration to another server, falling back to the server's public IP when the Cube has no DNS
            record yet. Identical to `host` from GET .../ssh, and the same value for every mapping on a Cube. Null only when
            the Cube has no server assigned, in which case there is nowhere to connect. Do NOT use `serverDomain` from the
            Cube object — that is the current physical host and changes when the Cube moves.
    """

    id: str
    cube_id: str
    cube_port: int
    host_port: int
    label: None | str
    status: str
    is_ssh: bool
    udp_enabled: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    whitelisted_ips: list[TcpMappingWhitelistedIpsItem]
    host: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        cube_id = self.cube_id

        cube_port = self.cube_port

        host_port = self.host_port

        label: None | str
        label = self.label

        status = self.status

        is_ssh = self.is_ssh

        udp_enabled = self.udp_enabled

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        whitelisted_ips = []
        for whitelisted_ips_item_data in self.whitelisted_ips:
            whitelisted_ips_item = whitelisted_ips_item_data.to_dict()
            whitelisted_ips.append(whitelisted_ips_item)

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "cubeId": cube_id,
                "cubePort": cube_port,
                "hostPort": host_port,
                "label": label,
                "status": status,
                "isSsh": is_ssh,
                "udpEnabled": udp_enabled,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "whitelistedIps": whitelisted_ips,
            }
        )
        if host is not UNSET:
            field_dict["host"] = host

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tcp_mapping_whitelisted_ips_item import (
            TcpMappingWhitelistedIpsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        cube_id = d.pop("cubeId")

        cube_port = d.pop("cubePort")

        host_port = d.pop("hostPort")

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))

        status = d.pop("status")

        is_ssh = d.pop("isSsh")

        udp_enabled = d.pop("udpEnabled")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        whitelisted_ips = []
        _whitelisted_ips = d.pop("whitelistedIps")
        for whitelisted_ips_item_data in _whitelisted_ips:
            whitelisted_ips_item = TcpMappingWhitelistedIpsItem.from_dict(
                whitelisted_ips_item_data
            )

            whitelisted_ips.append(whitelisted_ips_item)

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        tcp_mapping = cls(
            id=id,
            cube_id=cube_id,
            cube_port=cube_port,
            host_port=host_port,
            label=label,
            status=status,
            is_ssh=is_ssh,
            udp_enabled=udp_enabled,
            created_at=created_at,
            updated_at=updated_at,
            whitelisted_ips=whitelisted_ips,
            host=host,
        )

        tcp_mapping.additional_properties = d
        return tcp_mapping

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
