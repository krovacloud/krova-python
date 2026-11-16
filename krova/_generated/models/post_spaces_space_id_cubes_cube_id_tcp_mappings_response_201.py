from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tcp_mapping import TcpMapping


T = TypeVar("T", bound="PostSpacesSpaceIdCubesCubeIdTcpMappingsResponse201")


@_attrs_define
class PostSpacesSpaceIdCubesCubeIdTcpMappingsResponse201:
    """
    Attributes:
        tcp_mapping (TcpMapping):
    """

    tcp_mapping: TcpMapping
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tcp_mapping = self.tcp_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tcpMapping": tcp_mapping,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tcp_mapping import TcpMapping

        d = dict(src_dict)
        tcp_mapping = TcpMapping.from_dict(d.pop("tcpMapping"))

        post_spaces_space_id_cubes_cube_id_tcp_mappings_response_201 = cls(
            tcp_mapping=tcp_mapping,
        )

        post_spaces_space_id_cubes_cube_id_tcp_mappings_response_201.additional_properties = d
        return post_spaces_space_id_cubes_cube_id_tcp_mappings_response_201

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
