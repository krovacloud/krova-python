from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutSpacesSpaceIdCubesCubeIdSshPortBody")


@_attrs_define
class PutSpacesSpaceIdCubesCubeIdSshPortBody:
    """
    Attributes:
        cube_port (int): The port inside the Cube that sshd listens on (default 22). This is the Cube side of the
            mapping, not the host port.
    """

    cube_port: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cube_port = self.cube_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cubePort": cube_port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cube_port = d.pop("cubePort")

        put_spaces_space_id_cubes_cube_id_ssh_port_body = cls(
            cube_port=cube_port,
        )

        put_spaces_space_id_cubes_cube_id_ssh_port_body.additional_properties = d
        return put_spaces_space_id_cubes_cube_id_ssh_port_body

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
