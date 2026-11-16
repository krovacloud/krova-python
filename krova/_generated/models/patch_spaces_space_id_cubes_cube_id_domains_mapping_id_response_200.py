from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domain import Domain


T = TypeVar("T", bound="PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200")


@_attrs_define
class PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200:
    """
    Attributes:
        domain (Domain):
    """

    domain: Domain
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.domain import Domain

        d = dict(src_dict)
        domain = Domain.from_dict(d.pop("domain"))

        patch_spaces_space_id_cubes_cube_id_domains_mapping_id_response_200 = cls(
            domain=domain,
        )

        patch_spaces_space_id_cubes_cube_id_domains_mapping_id_response_200.additional_properties = d
        return patch_spaces_space_id_cubes_cube_id_domains_mapping_id_response_200

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
