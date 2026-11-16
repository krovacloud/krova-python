from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0")


@_attrs_define
class PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0:
    """Per-domain CORS policy, applied at the edge. Null (default) = CORS disabled and no Access-Control-* header is
    emitted anywhere. When set, the proxy answers OPTIONS preflight itself (204, the cube is never involved) and adds
    the headers to normal AND error responses, so a cross-origin request to a failing or stopped cube is never CORS-
    masked.

        Attributes:
            allowed_origins (list[str]): Exact scheme://host[:port] origins (no path, query or trailing slash), or the
                single-element wildcard ["*"]. "*" and allowCredentials are mutually exclusive.
            allowed_methods (list[str] | Unset): Allowed methods. Omitted = GET, POST, PUT, PATCH, DELETE, OPTIONS.
            allowed_headers (list[str] | Unset): Allowed request headers. Omitted/empty = echo the preflight's Access-
                Control-Request-Headers.
            exposed_headers (list[str] | Unset): Response headers exposed to JS. Omitted/empty = none.
            allow_credentials (bool | Unset): Send Access-Control-Allow-Credentials: true. Rejected together with the "*"
                origin.
            max_age_seconds (int | Unset): Preflight cache TTL. Default 600; 86400 is Chromium's hard cap.
    """

    allowed_origins: list[str]
    allowed_methods: list[str] | Unset = UNSET
    allowed_headers: list[str] | Unset = UNSET
    exposed_headers: list[str] | Unset = UNSET
    allow_credentials: bool | Unset = UNSET
    max_age_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_origins = self.allowed_origins

        allowed_methods: list[str] | Unset = UNSET
        if not isinstance(self.allowed_methods, Unset):
            allowed_methods = self.allowed_methods

        allowed_headers: list[str] | Unset = UNSET
        if not isinstance(self.allowed_headers, Unset):
            allowed_headers = self.allowed_headers

        exposed_headers: list[str] | Unset = UNSET
        if not isinstance(self.exposed_headers, Unset):
            exposed_headers = self.exposed_headers

        allow_credentials = self.allow_credentials

        max_age_seconds = self.max_age_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowedOrigins": allowed_origins,
            }
        )
        if allowed_methods is not UNSET:
            field_dict["allowedMethods"] = allowed_methods
        if allowed_headers is not UNSET:
            field_dict["allowedHeaders"] = allowed_headers
        if exposed_headers is not UNSET:
            field_dict["exposedHeaders"] = exposed_headers
        if allow_credentials is not UNSET:
            field_dict["allowCredentials"] = allow_credentials
        if max_age_seconds is not UNSET:
            field_dict["maxAgeSeconds"] = max_age_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allowed_origins = cast(list[str], d.pop("allowedOrigins"))

        allowed_methods = cast(list[str], d.pop("allowedMethods", UNSET))

        allowed_headers = cast(list[str], d.pop("allowedHeaders", UNSET))

        exposed_headers = cast(list[str], d.pop("exposedHeaders", UNSET))

        allow_credentials = d.pop("allowCredentials", UNSET)

        max_age_seconds = d.pop("maxAgeSeconds", UNSET)

        post_spaces_space_id_cubes_cube_id_domains_body_cors_config_type_0 = cls(
            allowed_origins=allowed_origins,
            allowed_methods=allowed_methods,
            allowed_headers=allowed_headers,
            exposed_headers=exposed_headers,
            allow_credentials=allow_credentials,
            max_age_seconds=max_age_seconds,
        )

        post_spaces_space_id_cubes_cube_id_domains_body_cors_config_type_0.additional_properties = d
        return post_spaces_space_id_cubes_cube_id_domains_body_cors_config_type_0

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
