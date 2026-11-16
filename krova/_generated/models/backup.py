from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_status import BackupStatus

if TYPE_CHECKING:
    from ..models.backup_config import BackupConfig


T = TypeVar("T", bound="Backup")


@_attrs_define
class Backup:
    """
    Attributes:
        id (str):
        name (str):
        status (BackupStatus):
        original_cube_id (str):
        original_cube_name (str):
        size_bytes (int | None):
        disk_size_gb (int):
        config (BackupConfig): The Cube configuration captured with the backup, used by redeploy. A shared copy carries
            no domains.
        shared_from_backup_id (None | str): Set on a shared copy: the backup it was shared from, which may since have
            been deleted. Null for a backup this space made itself.
        redeployed_cube_id (None | str):
        completed_at (datetime.datetime | None):
        created_at (datetime.datetime):
    """

    id: str
    name: str
    status: BackupStatus
    original_cube_id: str
    original_cube_name: str
    size_bytes: int | None
    disk_size_gb: int
    config: BackupConfig
    shared_from_backup_id: None | str
    redeployed_cube_id: None | str
    completed_at: datetime.datetime | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status.value

        original_cube_id = self.original_cube_id

        original_cube_name = self.original_cube_name

        size_bytes: int | None
        size_bytes = self.size_bytes

        disk_size_gb = self.disk_size_gb

        config = self.config.to_dict()

        shared_from_backup_id: None | str
        shared_from_backup_id = self.shared_from_backup_id

        redeployed_cube_id: None | str
        redeployed_cube_id = self.redeployed_cube_id

        completed_at: None | str
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "originalCubeId": original_cube_id,
                "originalCubeName": original_cube_name,
                "sizeBytes": size_bytes,
                "diskSizeGb": disk_size_gb,
                "config": config,
                "sharedFromBackupId": shared_from_backup_id,
                "redeployedCubeId": redeployed_cube_id,
                "completedAt": completed_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.backup_config import BackupConfig

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = BackupStatus(d.pop("status"))

        original_cube_id = d.pop("originalCubeId")

        original_cube_name = d.pop("originalCubeName")

        def _parse_size_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        size_bytes = _parse_size_bytes(d.pop("sizeBytes"))

        disk_size_gb = d.pop("diskSizeGb")

        config = BackupConfig.from_dict(d.pop("config"))

        def _parse_shared_from_backup_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        shared_from_backup_id = _parse_shared_from_backup_id(
            d.pop("sharedFromBackupId")
        )

        def _parse_redeployed_cube_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        redeployed_cube_id = _parse_redeployed_cube_id(d.pop("redeployedCubeId"))

        def _parse_completed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))

        created_at = isoparse(d.pop("createdAt"))

        backup = cls(
            id=id,
            name=name,
            status=status,
            original_cube_id=original_cube_id,
            original_cube_name=original_cube_name,
            size_bytes=size_bytes,
            disk_size_gb=disk_size_gb,
            config=config,
            shared_from_backup_id=shared_from_backup_id,
            redeployed_cube_id=redeployed_cube_id,
            completed_at=completed_at,
            created_at=created_at,
        )

        backup.additional_properties = d
        return backup

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
