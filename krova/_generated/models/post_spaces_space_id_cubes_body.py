from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_spaces_space_id_cubes_body_resources import (
        PostSpacesSpaceIdCubesBodyResources,
    )


T = TypeVar("T", bound="PostSpacesSpaceIdCubesBody")


@_attrs_define
class PostSpacesSpaceIdCubesBody:
    """
    Attributes:
        name (str):
        image (str):
        resources (PostSpacesSpaceIdCubesBodyResources):
        ssh_public_key (str): SSH public key written to the Cube login user's authorized_keys at boot
            (~/.ssh/authorized_keys for the ubuntu or debian user; /root/.ssh/authorized_keys on Cubes created before the
            default-user change). GET /cubes/{cubeId}/ssh reports the login user for a given Cube. Must start with ssh-
            ed25519, ssh-rsa, ecdsa-sha2-*, ssh-dss, or sk-*@openssh.com.
        region (str | Unset): Region slug from /v1/regions (optional).
        user_data (str | Unset): cloud-init script (max 16 KB, optional).
        termination_protection (bool | Unset): Create the Cube with termination protection already on, so it is never
            briefly deletable between create and a follow-up PATCH. Optional; anything other than a boolean is rejected with
            400. Default: False.
        idle_timeout_minutes (int | None | Unset): Minutes without activity after which Krova powers the Cube off. Null
            (the default) turns this off. A Cube counts as idle when no web terminal or SSH session is open and its CPU
            stays under 5% busy with a 5-minute load average under 0.1. Termination protection does not stop this power-off.
            Optional; an integer from 10 to 10080 (7 days) or null, anything else is rejected with 400.
    """

    name: str
    image: str
    resources: PostSpacesSpaceIdCubesBodyResources
    ssh_public_key: str
    region: str | Unset = UNSET
    user_data: str | Unset = UNSET
    termination_protection: bool | Unset = False
    idle_timeout_minutes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        image = self.image

        resources = self.resources.to_dict()

        ssh_public_key = self.ssh_public_key

        region = self.region

        user_data = self.user_data

        termination_protection = self.termination_protection

        idle_timeout_minutes: int | None | Unset
        if isinstance(self.idle_timeout_minutes, Unset):
            idle_timeout_minutes = UNSET
        else:
            idle_timeout_minutes = self.idle_timeout_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "image": image,
                "resources": resources,
                "sshPublicKey": ssh_public_key,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if user_data is not UNSET:
            field_dict["userData"] = user_data
        if termination_protection is not UNSET:
            field_dict["terminationProtection"] = termination_protection
        if idle_timeout_minutes is not UNSET:
            field_dict["idleTimeoutMinutes"] = idle_timeout_minutes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_spaces_space_id_cubes_body_resources import (
            PostSpacesSpaceIdCubesBodyResources,
        )

        d = dict(src_dict)
        name = d.pop("name")

        image = d.pop("image")

        resources = PostSpacesSpaceIdCubesBodyResources.from_dict(d.pop("resources"))

        ssh_public_key = d.pop("sshPublicKey")

        region = d.pop("region", UNSET)

        user_data = d.pop("userData", UNSET)

        termination_protection = d.pop("terminationProtection", UNSET)

        def _parse_idle_timeout_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idle_timeout_minutes = _parse_idle_timeout_minutes(
            d.pop("idleTimeoutMinutes", UNSET)
        )

        post_spaces_space_id_cubes_body = cls(
            name=name,
            image=image,
            resources=resources,
            ssh_public_key=ssh_public_key,
            region=region,
            user_data=user_data,
            termination_protection=termination_protection,
            idle_timeout_minutes=idle_timeout_minutes,
        )

        post_spaces_space_id_cubes_body.additional_properties = d
        return post_spaces_space_id_cubes_body

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
