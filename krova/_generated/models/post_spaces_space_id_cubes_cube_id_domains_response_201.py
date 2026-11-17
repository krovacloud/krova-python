from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dns_record import DnsRecord
    from ..models.domain import Domain


T = TypeVar("T", bound="PostSpacesSpaceIdCubesCubeIdDomainsResponse201")


@_attrs_define
class PostSpacesSpaceIdCubesCubeIdDomainsResponse201:
    """
    Attributes:
        domain (Domain):
        records (list[DnsRecord]):
    """

    domain: Domain
    records: list[DnsRecord]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain.to_dict()

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "records": records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dns_record import DnsRecord
        from ..models.domain import Domain

        d = dict(src_dict)
        domain = Domain.from_dict(d.pop("domain"))

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = DnsRecord.from_dict(records_item_data)

            records.append(records_item)

        post_spaces_space_id_cubes_cube_id_domains_response_201 = cls(
            domain=domain,
            records=records,
        )

        post_spaces_space_id_cubes_cube_id_domains_response_201.additional_properties = d
        return post_spaces_space_id_cubes_cube_id_domains_response_201

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
