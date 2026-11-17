from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tcp_mapping import TcpMapping


T = TypeVar("T", bound="GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200")


@_attrs_define
class GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200:
    """
    Attributes:
        tcp_mappings (list[TcpMapping]):
    """

    tcp_mappings: list[TcpMapping]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tcp_mappings = []
        for tcp_mappings_item_data in self.tcp_mappings:
            tcp_mappings_item = tcp_mappings_item_data.to_dict()
            tcp_mappings.append(tcp_mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tcpMappings": tcp_mappings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tcp_mapping import TcpMapping

        d = dict(src_dict)
        tcp_mappings = []
        _tcp_mappings = d.pop("tcpMappings")
        for tcp_mappings_item_data in _tcp_mappings:
            tcp_mappings_item = TcpMapping.from_dict(tcp_mappings_item_data)

            tcp_mappings.append(tcp_mappings_item)

        get_spaces_space_id_cubes_cube_id_tcp_mappings_response_200 = cls(
            tcp_mappings=tcp_mappings,
        )

        get_spaces_space_id_cubes_cube_id_tcp_mappings_response_200.additional_properties = d
        return get_spaces_space_id_cubes_cube_id_tcp_mappings_response_200

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
