from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_share_status import BackupShareStatus

T = TypeVar("T", bound="BackupShare")


@_attrs_define
class BackupShare:
    """
    Attributes:
        id (str):
        status (BackupShareStatus):
        backup_id (str): The SOURCE backup being shared.
        backup_name (str):
        source_space_id (str):
        destination_space_id (str):
        counterparty_space_name (str): The other space in this share: the destination on an outgoing share, the source
            on an incoming one.
        copy_backup_id (None | str): The destination space's own copy, once the share is accepted.
        expires_at (datetime.datetime):
        created_at (datetime.datetime):
    """

    id: str
    status: BackupShareStatus
    backup_id: str
    backup_name: str
    source_space_id: str
    destination_space_id: str
    counterparty_space_name: str
    copy_backup_id: None | str
    expires_at: datetime.datetime
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        backup_id = self.backup_id

        backup_name = self.backup_name

        source_space_id = self.source_space_id

        destination_space_id = self.destination_space_id

        counterparty_space_name = self.counterparty_space_name

        copy_backup_id: None | str
        copy_backup_id = self.copy_backup_id

        expires_at = self.expires_at.isoformat()

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "backupId": backup_id,
                "backupName": backup_name,
                "sourceSpaceId": source_space_id,
                "destinationSpaceId": destination_space_id,
                "counterpartySpaceName": counterparty_space_name,
                "copyBackupId": copy_backup_id,
                "expiresAt": expires_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        status = BackupShareStatus(d.pop("status"))

        backup_id = d.pop("backupId")

        backup_name = d.pop("backupName")

        source_space_id = d.pop("sourceSpaceId")

        destination_space_id = d.pop("destinationSpaceId")

        counterparty_space_name = d.pop("counterpartySpaceName")

        def _parse_copy_backup_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        copy_backup_id = _parse_copy_backup_id(d.pop("copyBackupId"))

        expires_at = isoparse(d.pop("expiresAt"))

        created_at = isoparse(d.pop("createdAt"))

        backup_share = cls(
            id=id,
            status=status,
            backup_id=backup_id,
            backup_name=backup_name,
            source_space_id=source_space_id,
            destination_space_id=destination_space_id,
            counterparty_space_name=counterparty_space_name,
            copy_backup_id=copy_backup_id,
            expires_at=expires_at,
            created_at=created_at,
        )

        backup_share.additional_properties = d
        return backup_share

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
