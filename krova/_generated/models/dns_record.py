from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dns_record_id import DnsRecordId
from ..models.dns_record_purpose import DnsRecordPurpose
from ..models.dns_record_type import DnsRecordType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsRecord")


@_attrs_define
class DnsRecord:
    """
    Attributes:
        id (DnsRecordId):
        type_ (DnsRecordType):
        host (str):
        value (str):
        purpose (DnsRecordPurpose):
        must_be_grey (bool):
        proxy_ok (bool):
        note (None | str | Unset):
    """

    id: DnsRecordId
    type_: DnsRecordType
    host: str
    value: str
    purpose: DnsRecordPurpose
    must_be_grey: bool
    proxy_ok: bool
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        type_ = self.type_.value

        host = self.host

        value = self.value

        purpose = self.purpose.value

        must_be_grey = self.must_be_grey

        proxy_ok = self.proxy_ok

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "host": host,
                "value": value,
                "purpose": purpose,
                "mustBeGrey": must_be_grey,
                "proxyOk": proxy_ok,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = DnsRecordId(d.pop("id"))

        type_ = DnsRecordType(d.pop("type"))

        host = d.pop("host")

        value = d.pop("value")

        purpose = DnsRecordPurpose(d.pop("purpose"))

        must_be_grey = d.pop("mustBeGrey")

        proxy_ok = d.pop("proxyOk")

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        dns_record = cls(
            id=id,
            type_=type_,
            host=host,
            value=value,
            purpose=purpose,
            must_be_grey=must_be_grey,
            proxy_ok=proxy_ok,
            note=note,
        )

        dns_record.additional_properties = d
        return dns_record

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
