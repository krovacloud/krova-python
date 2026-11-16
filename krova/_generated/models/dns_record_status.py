from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dns_record_status_state import DnsRecordStatusState
from ..models.dns_record_status_type import DnsRecordStatusType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsRecordStatus")


@_attrs_define
class DnsRecordStatus:
    """
    Attributes:
        id (str):
        type_ (DnsRecordStatusType):
        host (str):
        value (str):
        purpose (str):
        state (DnsRecordStatusState):
        detail (str):
        note (None | str | Unset):
        must_be_grey (bool | Unset):
        proxy_ok (bool | Unset):
        observed (list[str] | None | Unset):
    """

    id: str
    type_: DnsRecordStatusType
    host: str
    value: str
    purpose: str
    state: DnsRecordStatusState
    detail: str
    note: None | str | Unset = UNSET
    must_be_grey: bool | Unset = UNSET
    proxy_ok: bool | Unset = UNSET
    observed: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        host = self.host

        value = self.value

        purpose = self.purpose

        state = self.state.value

        detail = self.detail

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        must_be_grey = self.must_be_grey

        proxy_ok = self.proxy_ok

        observed: list[str] | None | Unset
        if isinstance(self.observed, Unset):
            observed = UNSET
        elif isinstance(self.observed, list):
            observed = self.observed

        else:
            observed = self.observed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "host": host,
                "value": value,
                "purpose": purpose,
                "state": state,
                "detail": detail,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if must_be_grey is not UNSET:
            field_dict["mustBeGrey"] = must_be_grey
        if proxy_ok is not UNSET:
            field_dict["proxyOk"] = proxy_ok
        if observed is not UNSET:
            field_dict["observed"] = observed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = DnsRecordStatusType(d.pop("type"))

        host = d.pop("host")

        value = d.pop("value")

        purpose = d.pop("purpose")

        state = DnsRecordStatusState(d.pop("state"))

        detail = d.pop("detail")

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        must_be_grey = d.pop("mustBeGrey", UNSET)

        proxy_ok = d.pop("proxyOk", UNSET)

        def _parse_observed(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                observed_type_0 = cast(list[str], data)

                return observed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        observed = _parse_observed(d.pop("observed", UNSET))

        dns_record_status = cls(
            id=id,
            type_=type_,
            host=host,
            value=value,
            purpose=purpose,
            state=state,
            detail=detail,
            note=note,
            must_be_grey=must_be_grey,
            proxy_ok=proxy_ok,
            observed=observed,
        )

        dns_record_status.additional_properties = d
        return dns_record_status

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
