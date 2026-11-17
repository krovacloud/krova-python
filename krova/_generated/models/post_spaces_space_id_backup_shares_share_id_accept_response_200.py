from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.backup import Backup
    from ..models.backup_share import BackupShare


T = TypeVar("T", bound="PostSpacesSpaceIdBackupSharesShareIdAcceptResponse200")


@_attrs_define
class PostSpacesSpaceIdBackupSharesShareIdAcceptResponse200:
    """
    Attributes:
        share (BackupShare):
        backup (Backup):
    """

    share: BackupShare
    backup: Backup
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share = self.share.to_dict()

        backup = self.backup.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "share": share,
                "backup": backup,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.backup import Backup
        from ..models.backup_share import BackupShare

        d = dict(src_dict)
        share = BackupShare.from_dict(d.pop("share"))

        backup = Backup.from_dict(d.pop("backup"))

        post_spaces_space_id_backup_shares_share_id_accept_response_200 = cls(
            share=share,
            backup=backup,
        )

        post_spaces_space_id_backup_shares_share_id_accept_response_200.additional_properties = d
        return post_spaces_space_id_backup_shares_share_id_accept_response_200

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
