from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_spaces_space_id_cubes_cube_id_resize_response_200_state import (
    PostSpacesSpaceIdCubesCubeIdResizeResponse200State,
)

if TYPE_CHECKING:
    from ..models.post_spaces_space_id_cubes_cube_id_resize_response_200_previous import (
        PostSpacesSpaceIdCubesCubeIdResizeResponse200Previous,
    )
    from ..models.post_spaces_space_id_cubes_cube_id_resize_response_200_requested import (
        PostSpacesSpaceIdCubesCubeIdResizeResponse200Requested,
    )


T = TypeVar("T", bound="PostSpacesSpaceIdCubesCubeIdResizeResponse200")


@_attrs_define
class PostSpacesSpaceIdCubesCubeIdResizeResponse200:
    """
    Attributes:
        success (bool):
        state (PostSpacesSpaceIdCubesCubeIdResizeResponse200State):
        job_id (str):
        is_live (bool): True when the resize is applied with no restart.
        requires_restart (bool): The inverse of `isLive`.
        previous (PostSpacesSpaceIdCubesCubeIdResizeResponse200Previous):
        requested (PostSpacesSpaceIdCubesCubeIdResizeResponse200Requested):
    """

    success: bool
    state: PostSpacesSpaceIdCubesCubeIdResizeResponse200State
    job_id: str
    is_live: bool
    requires_restart: bool
    previous: PostSpacesSpaceIdCubesCubeIdResizeResponse200Previous
    requested: PostSpacesSpaceIdCubesCubeIdResizeResponse200Requested
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        state = self.state.value

        job_id = self.job_id

        is_live = self.is_live

        requires_restart = self.requires_restart

        previous = self.previous.to_dict()

        requested = self.requested.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "state": state,
                "jobId": job_id,
                "isLive": is_live,
                "requiresRestart": requires_restart,
                "previous": previous,
                "requested": requested,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_spaces_space_id_cubes_cube_id_resize_response_200_previous import (
            PostSpacesSpaceIdCubesCubeIdResizeResponse200Previous,
        )
        from ..models.post_spaces_space_id_cubes_cube_id_resize_response_200_requested import (
            PostSpacesSpaceIdCubesCubeIdResizeResponse200Requested,
        )

        d = dict(src_dict)
        success = d.pop("success")

        state = PostSpacesSpaceIdCubesCubeIdResizeResponse200State(d.pop("state"))

        job_id = d.pop("jobId")

        is_live = d.pop("isLive")

        requires_restart = d.pop("requiresRestart")

        previous = PostSpacesSpaceIdCubesCubeIdResizeResponse200Previous.from_dict(
            d.pop("previous")
        )

        requested = PostSpacesSpaceIdCubesCubeIdResizeResponse200Requested.from_dict(
            d.pop("requested")
        )

        post_spaces_space_id_cubes_cube_id_resize_response_200 = cls(
            success=success,
            state=state,
            job_id=job_id,
            is_live=is_live,
            requires_restart=requires_restart,
            previous=previous,
            requested=requested,
        )

        post_spaces_space_id_cubes_cube_id_resize_response_200.additional_properties = d
        return post_spaces_space_id_cubes_cube_id_resize_response_200

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
