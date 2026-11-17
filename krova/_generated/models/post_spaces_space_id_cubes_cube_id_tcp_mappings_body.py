from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpacesSpaceIdCubesCubeIdTcpMappingsBody")


@_attrs_define
class PostSpacesSpaceIdCubesCubeIdTcpMappingsBody:
    """
    Attributes:
        cube_port (int):
        label (str | Unset): Optional human label for the mapping.
        whitelisted_ips (list[str] | Unset): IPs/CIDRs allowed to reach the published port. Omit or send an empty array
            to leave the port open to the internet.
        whitelist_ips (list[str] | Unset): DEPRECATED alias for `whitelistedIps`, accepted for backwards compatibility.
            `whitelistedIps` wins if both are sent. Use `whitelistedIps` in new code.
        udp_enabled (bool | Unset): Also forward UDP on this port. Defaults to true. Always false for the platform SSH
            mapping. The allowlist, if you send one, applies to both protocols. Default: True.
    """

    cube_port: int
    label: str | Unset = UNSET
    whitelisted_ips: list[str] | Unset = UNSET
    whitelist_ips: list[str] | Unset = UNSET
    udp_enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cube_port = self.cube_port

        label = self.label

        whitelisted_ips: list[str] | Unset = UNSET
        if not isinstance(self.whitelisted_ips, Unset):
            whitelisted_ips = self.whitelisted_ips

        whitelist_ips: list[str] | Unset = UNSET
        if not isinstance(self.whitelist_ips, Unset):
            whitelist_ips = self.whitelist_ips

        udp_enabled = self.udp_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cubePort": cube_port,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if whitelisted_ips is not UNSET:
            field_dict["whitelistedIps"] = whitelisted_ips
        if whitelist_ips is not UNSET:
            field_dict["whitelistIps"] = whitelist_ips
        if udp_enabled is not UNSET:
            field_dict["udpEnabled"] = udp_enabled

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cube_port = d.pop("cubePort")

        label = d.pop("label", UNSET)

        whitelisted_ips = cast(list[str], d.pop("whitelistedIps", UNSET))

        whitelist_ips = cast(list[str], d.pop("whitelistIps", UNSET))

        udp_enabled = d.pop("udpEnabled", UNSET)

        post_spaces_space_id_cubes_cube_id_tcp_mappings_body = cls(
            cube_port=cube_port,
            label=label,
            whitelisted_ips=whitelisted_ips,
            whitelist_ips=whitelist_ips,
            udp_enabled=udp_enabled,
        )

        post_spaces_space_id_cubes_cube_id_tcp_mappings_body.additional_properties = d
        return post_spaces_space_id_cubes_cube_id_tcp_mappings_body

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
