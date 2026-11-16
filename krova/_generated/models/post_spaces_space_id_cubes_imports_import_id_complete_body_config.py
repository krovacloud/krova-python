from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpacesSpaceIdCubesImportsImportIdCompleteBodyConfig")


@_attrs_define
class PostSpacesSpaceIdCubesImportsImportIdCompleteBodyConfig:
    """
    Attributes:
        vcpus (int):
        ram_mb (int):
        disk_limit_gb (int):
        image_id (str):
        user_data (None | str | Unset):
    """

    vcpus: int
    ram_mb: int
    disk_limit_gb: int
    image_id: str
    user_data: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vcpus = self.vcpus

        ram_mb = self.ram_mb

        disk_limit_gb = self.disk_limit_gb

        image_id = self.image_id

        user_data: None | str | Unset
        if isinstance(self.user_data, Unset):
            user_data = UNSET
        else:
            user_data = self.user_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vcpus": vcpus,
                "ramMb": ram_mb,
                "diskLimitGb": disk_limit_gb,
                "imageId": image_id,
            }
        )
        if user_data is not UNSET:
            field_dict["userData"] = user_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vcpus = d.pop("vcpus")

        ram_mb = d.pop("ramMb")

        disk_limit_gb = d.pop("diskLimitGb")

        image_id = d.pop("imageId")

        def _parse_user_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_data = _parse_user_data(d.pop("userData", UNSET))

        post_spaces_space_id_cubes_imports_import_id_complete_body_config = cls(
            vcpus=vcpus,
            ram_mb=ram_mb,
            disk_limit_gb=disk_limit_gb,
            image_id=image_id,
            user_data=user_data,
        )

        post_spaces_space_id_cubes_imports_import_id_complete_body_config.additional_properties = d
        return post_spaces_space_id_cubes_imports_import_id_complete_body_config

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
