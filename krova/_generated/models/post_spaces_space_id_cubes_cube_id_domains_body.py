from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_spaces_space_id_cubes_cube_id_domains_body_origin_scheme import (
    PostSpacesSpaceIdCubesCubeIdDomainsBodyOriginScheme,
)
from ..models.post_spaces_space_id_cubes_cube_id_domains_body_proxy_protocol import (
    PostSpacesSpaceIdCubesCubeIdDomainsBodyProxyProtocol,
)
from ..models.post_spaces_space_id_cubes_cube_id_domains_body_security_headers_mode import (
    PostSpacesSpaceIdCubesCubeIdDomainsBodySecurityHeadersMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_spaces_space_id_cubes_cube_id_domains_body_cors_config_type_0 import (
        PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0,
    )
    from ..models.post_spaces_space_id_cubes_cube_id_domains_body_request_header_overrides_type_0 import (
        PostSpacesSpaceIdCubesCubeIdDomainsBodyRequestHeaderOverridesType0,
    )
    from ..models.post_spaces_space_id_cubes_cube_id_domains_body_response_header_overrides_type_0 import (
        PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0,
    )


T = TypeVar("T", bound="PostSpacesSpaceIdCubesCubeIdDomainsBody")


@_attrs_define
class PostSpacesSpaceIdCubesCubeIdDomainsBody:
    """
    Attributes:
        domain (str): The hostname to attach, e.g. app.example.com
        port (int): Cube port the domain proxies to.
        security_headers_mode (PostSpacesSpaceIdCubesCubeIdDomainsBodySecurityHeadersMode | Unset): enforced = proxy
            sets platform security headers (HSTS, X-Frame-Options, …); app_managed = the app's own headers pass through.
            Default enforced.
        response_header_timeout_secs (int | Unset): Seconds the app may take to send response headers (streaming
            unaffected). Default 60.
        response_header_overrides (None | PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0 | Unset):
            Header rewrites: `set` adds/overwrites, `remove` deletes. Null clears all.
        request_header_overrides (None | PostSpacesSpaceIdCubesCubeIdDomainsBodyRequestHeaderOverridesType0 | Unset):
            Header rewrites: `set` adds/overwrites, `remove` deletes. Null clears all.
        max_request_body_mb (int | None | Unset): Max request body size (MB). Null = unlimited (default).
        cors_config (None | PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0 | Unset): Per-domain CORS policy,
            applied at the edge. Null (default) = CORS disabled and no Access-Control-* header is emitted anywhere. When
            set, the proxy answers OPTIONS preflight itself (204, the cube is never involved) and adds the headers to normal
            AND error responses, so a cross-origin request to a failing or stopped cube is never CORS-masked.
        origin_scheme (PostSpacesSpaceIdCubesCubeIdDomainsBodyOriginScheme | Unset): Scheme the edge speaks to the CUBE
            on the backend hop. http (default) = cleartext. https = the cube terminates TLS itself (a control panel holding
            its own certificate, or an app listening on HTTPS) and answers plain HTTP with a redirect, so it cannot be
            reached over cleartext at all. Visitors are on HTTPS either way. The dial port is derived: https on the default
            port 80 connects on 443; a deliberate custom port is honored exactly. Applied as saved: if the cube does not
            serve this hostname over HTTPS, requests to the domain fail until you set it back to http.
        proxy_protocol (PostSpacesSpaceIdCubesCubeIdDomainsBodyProxyProtocol | Unset): Send a PROXY protocol header (v1
            text or v2 binary) at the start of every connection to the cube, so the app reads the visitor's address from the
            connection itself, as on a plain VPS. Null (default) = off. The app must accept PROXY protocol on this port, or
            every request to the domain fails; it is applied as saved. Every domain on the same cube port must use the same
            setting: a save that would mix them is refused with 409 unless confirmMixedProxyProtocol is true.
        confirm_mixed_proxy_protocol (bool | Unset): Accept a save that leaves domains on the same cube port with
            different proxyProtocol settings (for an app that handles both on one port, or mid-migration). Not stored.
        response_compression (bool | Unset): Edge gzip/zstd compression. Default false (domains behind a CDN are already
            compressed there).
        ip_allow_list (list[str] | None | Unset): Visitor IP/CIDR allow-list (v4+v6). Non-empty ⇒ only these reach the
            app. Null/empty = open.
        ip_deny_list (list[str] | None | Unset): Visitor IP/CIDR deny-list (v4+v6) → 403. Null/empty = none.
        basic_auth_user (None | str | Unset): HTTP Basic Auth username. Null/empty clears Basic Auth. Setting it
            requires basicAuthPassword.
        basic_auth_password (str | Unset): Plaintext Basic Auth password — bcrypt-hashed server-side, never stored or
            returned. Required when setting basicAuthUser.
    """

    domain: str
    port: int
    security_headers_mode: (
        PostSpacesSpaceIdCubesCubeIdDomainsBodySecurityHeadersMode | Unset
    ) = UNSET
    response_header_timeout_secs: int | Unset = UNSET
    response_header_overrides: (
        None
        | PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0
        | Unset
    ) = UNSET
    request_header_overrides: (
        None
        | PostSpacesSpaceIdCubesCubeIdDomainsBodyRequestHeaderOverridesType0
        | Unset
    ) = UNSET
    max_request_body_mb: int | None | Unset = UNSET
    cors_config: (
        None | PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0 | Unset
    ) = UNSET
    origin_scheme: PostSpacesSpaceIdCubesCubeIdDomainsBodyOriginScheme | Unset = UNSET
    proxy_protocol: PostSpacesSpaceIdCubesCubeIdDomainsBodyProxyProtocol | Unset = UNSET
    confirm_mixed_proxy_protocol: bool | Unset = UNSET
    response_compression: bool | Unset = UNSET
    ip_allow_list: list[str] | None | Unset = UNSET
    ip_deny_list: list[str] | None | Unset = UNSET
    basic_auth_user: None | str | Unset = UNSET
    basic_auth_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_spaces_space_id_cubes_cube_id_domains_body_cors_config_type_0 import (
            PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0,
        )
        from ..models.post_spaces_space_id_cubes_cube_id_domains_body_request_header_overrides_type_0 import (
            PostSpacesSpaceIdCubesCubeIdDomainsBodyRequestHeaderOverridesType0,
        )
        from ..models.post_spaces_space_id_cubes_cube_id_domains_body_response_header_overrides_type_0 import (
            PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0,
        )

        domain = self.domain

        port = self.port

        security_headers_mode: str | Unset = UNSET
        if not isinstance(self.security_headers_mode, Unset):
            security_headers_mode = self.security_headers_mode.value

        response_header_timeout_secs = self.response_header_timeout_secs

        response_header_overrides: dict[str, Any] | None | Unset
        if isinstance(self.response_header_overrides, Unset):
            response_header_overrides = UNSET
        elif isinstance(
            self.response_header_overrides,
            PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0,
        ):
            response_header_overrides = self.response_header_overrides.to_dict()
        else:
            response_header_overrides = self.response_header_overrides

        request_header_overrides: dict[str, Any] | None | Unset
        if isinstance(self.request_header_overrides, Unset):
            request_header_overrides = UNSET
        elif isinstance(
            self.request_header_overrides,
            PostSpacesSpaceIdCubesCubeIdDomainsBodyRequestHeaderOverridesType0,
        ):
            request_header_overrides = self.request_header_overrides.to_dict()
        else:
            request_header_overrides = self.request_header_overrides

        max_request_body_mb: int | None | Unset
        if isinstance(self.max_request_body_mb, Unset):
            max_request_body_mb = UNSET
        else:
            max_request_body_mb = self.max_request_body_mb

        cors_config: dict[str, Any] | None | Unset
        if isinstance(self.cors_config, Unset):
            cors_config = UNSET
        elif isinstance(
            self.cors_config, PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0
        ):
            cors_config = self.cors_config.to_dict()
        else:
            cors_config = self.cors_config

        origin_scheme: str | Unset = UNSET
        if not isinstance(self.origin_scheme, Unset):
            origin_scheme = self.origin_scheme.value

        proxy_protocol: str | Unset = UNSET
        if not isinstance(self.proxy_protocol, Unset):
            proxy_protocol = self.proxy_protocol.value

        confirm_mixed_proxy_protocol = self.confirm_mixed_proxy_protocol

        response_compression = self.response_compression

        ip_allow_list: list[str] | None | Unset
        if isinstance(self.ip_allow_list, Unset):
            ip_allow_list = UNSET
        elif isinstance(self.ip_allow_list, list):
            ip_allow_list = self.ip_allow_list

        else:
            ip_allow_list = self.ip_allow_list

        ip_deny_list: list[str] | None | Unset
        if isinstance(self.ip_deny_list, Unset):
            ip_deny_list = UNSET
        elif isinstance(self.ip_deny_list, list):
            ip_deny_list = self.ip_deny_list

        else:
            ip_deny_list = self.ip_deny_list

        basic_auth_user: None | str | Unset
        if isinstance(self.basic_auth_user, Unset):
            basic_auth_user = UNSET
        else:
            basic_auth_user = self.basic_auth_user

        basic_auth_password = self.basic_auth_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "port": port,
            }
        )
        if security_headers_mode is not UNSET:
            field_dict["securityHeadersMode"] = security_headers_mode
        if response_header_timeout_secs is not UNSET:
            field_dict["responseHeaderTimeoutSecs"] = response_header_timeout_secs
        if response_header_overrides is not UNSET:
            field_dict["responseHeaderOverrides"] = response_header_overrides
        if request_header_overrides is not UNSET:
            field_dict["requestHeaderOverrides"] = request_header_overrides
        if max_request_body_mb is not UNSET:
            field_dict["maxRequestBodyMb"] = max_request_body_mb
        if cors_config is not UNSET:
            field_dict["corsConfig"] = cors_config
        if origin_scheme is not UNSET:
            field_dict["originScheme"] = origin_scheme
        if proxy_protocol is not UNSET:
            field_dict["proxyProtocol"] = proxy_protocol
        if confirm_mixed_proxy_protocol is not UNSET:
            field_dict["confirmMixedProxyProtocol"] = confirm_mixed_proxy_protocol
        if response_compression is not UNSET:
            field_dict["responseCompression"] = response_compression
        if ip_allow_list is not UNSET:
            field_dict["ipAllowList"] = ip_allow_list
        if ip_deny_list is not UNSET:
            field_dict["ipDenyList"] = ip_deny_list
        if basic_auth_user is not UNSET:
            field_dict["basicAuthUser"] = basic_auth_user
        if basic_auth_password is not UNSET:
            field_dict["basicAuthPassword"] = basic_auth_password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_spaces_space_id_cubes_cube_id_domains_body_cors_config_type_0 import (
            PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0,
        )
        from ..models.post_spaces_space_id_cubes_cube_id_domains_body_request_header_overrides_type_0 import (
            PostSpacesSpaceIdCubesCubeIdDomainsBodyRequestHeaderOverridesType0,
        )
        from ..models.post_spaces_space_id_cubes_cube_id_domains_body_response_header_overrides_type_0 import (
            PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0,
        )

        d = dict(src_dict)
        domain = d.pop("domain")

        port = d.pop("port")

        _security_headers_mode = d.pop("securityHeadersMode", UNSET)
        security_headers_mode: (
            PostSpacesSpaceIdCubesCubeIdDomainsBodySecurityHeadersMode | Unset
        )
        if isinstance(_security_headers_mode, Unset):
            security_headers_mode = UNSET
        else:
            security_headers_mode = (
                PostSpacesSpaceIdCubesCubeIdDomainsBodySecurityHeadersMode(
                    _security_headers_mode
                )
            )

        response_header_timeout_secs = d.pop("responseHeaderTimeoutSecs", UNSET)

        def _parse_response_header_overrides(
            data: object,
        ) -> (
            None
            | PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_header_overrides_type_0 = PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0.from_dict(
                    data
                )

                return response_header_overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PostSpacesSpaceIdCubesCubeIdDomainsBodyResponseHeaderOverridesType0
                | Unset,
                data,
            )

        response_header_overrides = _parse_response_header_overrides(
            d.pop("responseHeaderOverrides", UNSET)
        )

        def _parse_request_header_overrides(
            data: object,
        ) -> (
            None
            | PostSpacesSpaceIdCubesCubeIdDomainsBodyRequestHeaderOverridesType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_header_overrides_type_0 = PostSpacesSpaceIdCubesCubeIdDomainsBodyRequestHeaderOverridesType0.from_dict(
                    data
                )

                return request_header_overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PostSpacesSpaceIdCubesCubeIdDomainsBodyRequestHeaderOverridesType0
                | Unset,
                data,
            )

        request_header_overrides = _parse_request_header_overrides(
            d.pop("requestHeaderOverrides", UNSET)
        )

        def _parse_max_request_body_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_request_body_mb = _parse_max_request_body_mb(
            d.pop("maxRequestBodyMb", UNSET)
        )

        def _parse_cors_config(
            data: object,
        ) -> None | PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cors_config_type_0 = (
                    PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0.from_dict(
                        data
                    )
                )

                return cors_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PostSpacesSpaceIdCubesCubeIdDomainsBodyCorsConfigType0 | Unset,
                data,
            )

        cors_config = _parse_cors_config(d.pop("corsConfig", UNSET))

        _origin_scheme = d.pop("originScheme", UNSET)
        origin_scheme: PostSpacesSpaceIdCubesCubeIdDomainsBodyOriginScheme | Unset
        if isinstance(_origin_scheme, Unset):
            origin_scheme = UNSET
        else:
            origin_scheme = PostSpacesSpaceIdCubesCubeIdDomainsBodyOriginScheme(
                _origin_scheme
            )

        _proxy_protocol = d.pop("proxyProtocol", UNSET)
        proxy_protocol: PostSpacesSpaceIdCubesCubeIdDomainsBodyProxyProtocol | Unset
        if isinstance(_proxy_protocol, Unset):
            proxy_protocol = UNSET
        else:
            proxy_protocol = PostSpacesSpaceIdCubesCubeIdDomainsBodyProxyProtocol(
                _proxy_protocol
            )

        confirm_mixed_proxy_protocol = d.pop("confirmMixedProxyProtocol", UNSET)

        response_compression = d.pop("responseCompression", UNSET)

        def _parse_ip_allow_list(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_allow_list_type_0 = cast(list[str], data)

                return ip_allow_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ip_allow_list = _parse_ip_allow_list(d.pop("ipAllowList", UNSET))

        def _parse_ip_deny_list(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_deny_list_type_0 = cast(list[str], data)

                return ip_deny_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ip_deny_list = _parse_ip_deny_list(d.pop("ipDenyList", UNSET))

        def _parse_basic_auth_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        basic_auth_user = _parse_basic_auth_user(d.pop("basicAuthUser", UNSET))

        basic_auth_password = d.pop("basicAuthPassword", UNSET)

        post_spaces_space_id_cubes_cube_id_domains_body = cls(
            domain=domain,
            port=port,
            security_headers_mode=security_headers_mode,
            response_header_timeout_secs=response_header_timeout_secs,
            response_header_overrides=response_header_overrides,
            request_header_overrides=request_header_overrides,
            max_request_body_mb=max_request_body_mb,
            cors_config=cors_config,
            origin_scheme=origin_scheme,
            proxy_protocol=proxy_protocol,
            confirm_mixed_proxy_protocol=confirm_mixed_proxy_protocol,
            response_compression=response_compression,
            ip_allow_list=ip_allow_list,
            ip_deny_list=ip_deny_list,
            basic_auth_user=basic_auth_user,
            basic_auth_password=basic_auth_password,
        )

        post_spaces_space_id_cubes_cube_id_domains_body.additional_properties = d
        return post_spaces_space_id_cubes_cube_id_domains_body

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
