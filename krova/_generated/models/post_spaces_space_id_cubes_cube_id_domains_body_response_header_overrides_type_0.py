from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_spaces_space_id_cubes_cube_id_domains_body_response_header_overrides_type_0_set import (
        PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0Set,
    )


T = TypeVar(
    "T", bound="PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0"
)


@_attrs_define
class PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0:
    """Header rewrites: `set` adds/overwrites, `remove` deletes. Null clears all.

    Attributes:
        set_ (PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0Set | Unset):
        remove (list[str] | Unset):
    """

    set_: (
        PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0Set | Unset
    ) = UNSET
    remove: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_, Unset):
            set_ = self.set_.to_dict()

        remove: list[str] | Unset = UNSET
        if not isinstance(self.remove, Unset):
            remove = self.remove

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if set_ is not UNSET:
            field_dict["set"] = set_
        if remove is not UNSET:
            field_dict["remove"] = remove

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_spaces_space_id_cubes_cube_id_domains_body_response_header_overrides_type_0_set import (
            PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0Set,
        )

        d = dict(src_dict)
        _set_ = d.pop("set", UNSET)
        set_: (
            PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0Set
            | Unset
        )
        if isinstance(_set_, Unset):
            set_ = UNSET
        else:
            set_ = PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0Set.from_dict(
                _set_
            )

        remove = cast(list[str], d.pop("remove", UNSET))

        post_spaces_space_id_cubes_cube_id_domains_body_response_header_overrides_type_0 = cls(
            set_=set_,
            remove=remove,
        )

        post_spaces_space_id_cubes_cube_id_domains_body_response_header_overrides_type_0.additional_properties = d
        return post_spaces_space_id_cubes_cube_id_domains_body_response_header_overrides_type_0

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
