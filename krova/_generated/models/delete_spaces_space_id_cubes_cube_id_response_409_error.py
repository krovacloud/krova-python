from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_spaces_space_id_cubes_cube_id_response_409_error_code import (
    DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_spaces_space_id_cubes_cube_id_response_409_error_cube import (
        DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCube,
    )


T = TypeVar("T", bound="DeleteSpacesSpaceIdCubesCubeIdResponse409Error")


@_attrs_define
class DeleteSpacesSpaceIdCubesCubeIdResponse409Error:
    """
    Attributes:
        code (DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCode):
        message (str):
        cube (DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCube | Unset):
    """

    code: DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCode
    message: str
    cube: DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCube | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        cube: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cube, Unset):
            cube = self.cube.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if cube is not UNSET:
            field_dict["cube"] = cube

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.delete_spaces_space_id_cubes_cube_id_response_409_error_cube import (
            DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCube,
        )

        d = dict(src_dict)
        code = DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCode(d.pop("code"))

        message = d.pop("message")

        _cube = d.pop("cube", UNSET)
        cube: DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCube | Unset
        if isinstance(_cube, Unset):
            cube = UNSET
        else:
            cube = DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCube.from_dict(_cube)

        delete_spaces_space_id_cubes_cube_id_response_409_error = cls(
            code=code,
            message=message,
            cube=cube,
        )

        delete_spaces_space_id_cubes_cube_id_response_409_error.additional_properties = d
        return delete_spaces_space_id_cubes_cube_id_response_409_error

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
