from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostAuthCliStartResponse200")


@_attrs_define
class PostAuthCliStartResponse200:
    """
    Attributes:
        device_code (str): High-entropy code the CLI keeps secret and presents on each poll. Only its hash is stored
            server-side.
        user_code (str): Short human-readable code (KROVA-XXXX-XXXX) the user confirms in the browser.
        verification_uri (str): Browser URL where the user approves.
        verification_uri_complete (str): verificationUri with the user code pre-filled.
        interval (int): Seconds to wait between polls.
        expires_in (int): Seconds until the device code expires (~600).
    """

    device_code: str
    user_code: str
    verification_uri: str
    verification_uri_complete: str
    interval: int
    expires_in: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_code = self.device_code

        user_code = self.user_code

        verification_uri = self.verification_uri

        verification_uri_complete = self.verification_uri_complete

        interval = self.interval

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceCode": device_code,
                "userCode": user_code,
                "verificationUri": verification_uri,
                "verificationUriComplete": verification_uri_complete,
                "interval": interval,
                "expiresIn": expires_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_code = d.pop("deviceCode")

        user_code = d.pop("userCode")

        verification_uri = d.pop("verificationUri")

        verification_uri_complete = d.pop("verificationUriComplete")

        interval = d.pop("interval")

        expires_in = d.pop("expiresIn")

        post_auth_cli_start_response_200 = cls(
            device_code=device_code,
            user_code=user_code,
            verification_uri=verification_uri,
            verification_uri_complete=verification_uri_complete,
            interval=interval,
            expires_in=expires_in,
        )

        post_auth_cli_start_response_200.additional_properties = d
        return post_auth_cli_start_response_200

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
