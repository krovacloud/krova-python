from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.dns_record_status import DnsRecordStatus
    from ..models.get_spaces_space_id_cubes_cube_id_domains_mapping_id_records_response_200_summary import (
        GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200Summary,
    )


T = TypeVar("T", bound="GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200")


@_attrs_define
class GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200:
    """
    Attributes:
        domain (str):
        is_wildcard (bool):
        records (list[DnsRecordStatus]):
        summary (GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200Summary):
        checked_at (datetime.datetime):
    """

    domain: str
    is_wildcard: bool
    records: list[DnsRecordStatus]
    summary: GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200Summary
    checked_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        is_wildcard = self.is_wildcard

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        summary = self.summary.to_dict()

        checked_at = self.checked_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "isWildcard": is_wildcard,
                "records": records,
                "summary": summary,
                "checkedAt": checked_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dns_record_status import DnsRecordStatus
        from ..models.get_spaces_space_id_cubes_cube_id_domains_mapping_id_records_response_200_summary import (
            GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200Summary,
        )

        d = dict(src_dict)
        domain = d.pop("domain")

        is_wildcard = d.pop("isWildcard")

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = DnsRecordStatus.from_dict(records_item_data)

            records.append(records_item)

        summary = GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200Summary.from_dict(
            d.pop("summary")
        )

        checked_at = isoparse(d.pop("checkedAt"))

        get_spaces_space_id_cubes_cube_id_domains_mapping_id_records_response_200 = cls(
            domain=domain,
            is_wildcard=is_wildcard,
            records=records,
            summary=summary,
            checked_at=checked_at,
        )

        get_spaces_space_id_cubes_cube_id_domains_mapping_id_records_response_200.additional_properties = d
        return get_spaces_space_id_cubes_cube_id_domains_mapping_id_records_response_200

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
