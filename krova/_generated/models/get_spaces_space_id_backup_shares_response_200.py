from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.backup_share import BackupShare


T = TypeVar("T", bound="GetSpacesSpaceIdBackupSharesResponse200")


@_attrs_define
class GetSpacesSpaceIdBackupSharesResponse200:
    """
    Attributes:
        incoming (list[BackupShare]):
        outgoing (list[BackupShare]):
    """

    incoming: list[BackupShare]
    outgoing: list[BackupShare]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incoming = []
        for incoming_item_data in self.incoming:
            incoming_item = incoming_item_data.to_dict()
            incoming.append(incoming_item)

        outgoing = []
        for outgoing_item_data in self.outgoing:
            outgoing_item = outgoing_item_data.to_dict()
            outgoing.append(outgoing_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incoming": incoming,
                "outgoing": outgoing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.backup_share import BackupShare

        d = dict(src_dict)
        incoming = []
        _incoming = d.pop("incoming")
        for incoming_item_data in _incoming:
            incoming_item = BackupShare.from_dict(incoming_item_data)

            incoming.append(incoming_item)

        outgoing = []
        _outgoing = d.pop("outgoing")
        for outgoing_item_data in _outgoing:
            outgoing_item = BackupShare.from_dict(outgoing_item_data)

            outgoing.append(outgoing_item)

        get_spaces_space_id_backup_shares_response_200 = cls(
            incoming=incoming,
            outgoing=outgoing,
        )

        get_spaces_space_id_backup_shares_response_200.additional_properties = d
        return get_spaces_space_id_backup_shares_response_200

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
