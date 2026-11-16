from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_spaces_space_id_cubes_imports_body_ssh_key_mode import (
    PostSpacesSpaceIdCubesImportsBodySshKeyMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_spaces_space_id_cubes_imports_body_expected_config_type_0 import (
        PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0,
    )


T = TypeVar("T", bound="PostSpacesSpaceIdCubesImportsBody")


@_attrs_define
class PostSpacesSpaceIdCubesImportsBody:
    """
    Attributes:
        name (str):
        file_size_bytes (int):
        ssh_key_mode (PostSpacesSpaceIdCubesImportsBodySshKeyMode | Unset): What to do with SSH access on the imported
            rootfs. `replace` (default) writes `sshPublicKey` to the login user's authorized_keys and requires
            `sshPublicKey` to be set. `keep` leaves the image's own authorized_keys and sshd configuration completely
            untouched — nothing is written — so you must already hold a private key that the image accepts, or you will not
            be able to log in. Default: PostSpacesSpaceIdCubesImportsBodySshKeyMode.REPLACE.
        ssh_public_key (None | str | Unset): Public key to install when `sshKeyMode` is `replace`. Written to the login
            user's `~/.ssh/authorized_keys` — which user that is comes from the imported rootfs itself, so an image without
            a Krova default user keeps logging in as root. Ignored when `sshKeyMode` is `keep`.
        region (None | str | Unset):
        vcpus_override (int | None | Unset):
        ram_mb_override (int | None | Unset):
        disk_gb_override (int | None | Unset):
        user_data (None | str | Unset):
        expected_config (None | PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0 | Unset):
    """

    name: str
    file_size_bytes: int
    ssh_key_mode: PostSpacesSpaceIdCubesImportsBodySshKeyMode | Unset = (
        PostSpacesSpaceIdCubesImportsBodySshKeyMode.REPLACE
    )
    ssh_public_key: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    vcpus_override: int | None | Unset = UNSET
    ram_mb_override: int | None | Unset = UNSET
    disk_gb_override: int | None | Unset = UNSET
    user_data: None | str | Unset = UNSET
    expected_config: (
        None | PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_spaces_space_id_cubes_imports_body_expected_config_type_0 import (
            PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0,
        )

        name = self.name

        file_size_bytes = self.file_size_bytes

        ssh_key_mode: str | Unset = UNSET
        if not isinstance(self.ssh_key_mode, Unset):
            ssh_key_mode = self.ssh_key_mode.value

        ssh_public_key: None | str | Unset
        if isinstance(self.ssh_public_key, Unset):
            ssh_public_key = UNSET
        else:
            ssh_public_key = self.ssh_public_key

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        vcpus_override: int | None | Unset
        if isinstance(self.vcpus_override, Unset):
            vcpus_override = UNSET
        else:
            vcpus_override = self.vcpus_override

        ram_mb_override: int | None | Unset
        if isinstance(self.ram_mb_override, Unset):
            ram_mb_override = UNSET
        else:
            ram_mb_override = self.ram_mb_override

        disk_gb_override: int | None | Unset
        if isinstance(self.disk_gb_override, Unset):
            disk_gb_override = UNSET
        else:
            disk_gb_override = self.disk_gb_override

        user_data: None | str | Unset
        if isinstance(self.user_data, Unset):
            user_data = UNSET
        else:
            user_data = self.user_data

        expected_config: dict[str, Any] | None | Unset
        if isinstance(self.expected_config, Unset):
            expected_config = UNSET
        elif isinstance(
            self.expected_config, PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0
        ):
            expected_config = self.expected_config.to_dict()
        else:
            expected_config = self.expected_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "fileSizeBytes": file_size_bytes,
            }
        )
        if ssh_key_mode is not UNSET:
            field_dict["sshKeyMode"] = ssh_key_mode
        if ssh_public_key is not UNSET:
            field_dict["sshPublicKey"] = ssh_public_key
        if region is not UNSET:
            field_dict["region"] = region
        if vcpus_override is not UNSET:
            field_dict["vcpusOverride"] = vcpus_override
        if ram_mb_override is not UNSET:
            field_dict["ramMbOverride"] = ram_mb_override
        if disk_gb_override is not UNSET:
            field_dict["diskGbOverride"] = disk_gb_override
        if user_data is not UNSET:
            field_dict["userData"] = user_data
        if expected_config is not UNSET:
            field_dict["expectedConfig"] = expected_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_spaces_space_id_cubes_imports_body_expected_config_type_0 import (
            PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        file_size_bytes = d.pop("fileSizeBytes")

        _ssh_key_mode = d.pop("sshKeyMode", UNSET)
        ssh_key_mode: PostSpacesSpaceIdCubesImportsBodySshKeyMode | Unset
        if isinstance(_ssh_key_mode, Unset):
            ssh_key_mode = UNSET
        else:
            ssh_key_mode = PostSpacesSpaceIdCubesImportsBodySshKeyMode(_ssh_key_mode)

        def _parse_ssh_public_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_public_key = _parse_ssh_public_key(d.pop("sshPublicKey", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_vcpus_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vcpus_override = _parse_vcpus_override(d.pop("vcpusOverride", UNSET))

        def _parse_ram_mb_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ram_mb_override = _parse_ram_mb_override(d.pop("ramMbOverride", UNSET))

        def _parse_disk_gb_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        disk_gb_override = _parse_disk_gb_override(d.pop("diskGbOverride", UNSET))

        def _parse_user_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_data = _parse_user_data(d.pop("userData", UNSET))

        def _parse_expected_config(
            data: object,
        ) -> None | PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                expected_config_type_0 = (
                    PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0.from_dict(data)
                )

                return expected_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PostSpacesSpaceIdCubesImportsBodyExpectedConfigType0 | Unset,
                data,
            )

        expected_config = _parse_expected_config(d.pop("expectedConfig", UNSET))

        post_spaces_space_id_cubes_imports_body = cls(
            name=name,
            file_size_bytes=file_size_bytes,
            ssh_key_mode=ssh_key_mode,
            ssh_public_key=ssh_public_key,
            region=region,
            vcpus_override=vcpus_override,
            ram_mb_override=ram_mb_override,
            disk_gb_override=disk_gb_override,
            user_data=user_data,
            expected_config=expected_config,
        )

        post_spaces_space_id_cubes_imports_body.additional_properties = d
        return post_spaces_space_id_cubes_imports_body

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
