from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_origin_scheme import DomainOriginScheme
from ..models.domain_proxy_protocol import DomainProxyProtocol
from ..models.domain_security_headers_mode import DomainSecurityHeadersMode
from ..models.domain_wildcard_cert_state import DomainWildcardCertState

if TYPE_CHECKING:
    from ..models.domain_cors_config_type_0 import DomainCorsConfigType0
    from ..models.domain_request_header_overrides_type_0 import (
        DomainRequestHeaderOverridesType0,
    )
    from ..models.domain_response_header_overrides_type_0 import (
        DomainResponseHeaderOverridesType0,
    )


T = TypeVar("T", bound="Domain")


@_attrs_define
class Domain:
    """
    Attributes:
        id (str):
        cube_id (str):
        domain (str):
        port (int | None):
        status (str):
        ingress_status (None | str):
        security_headers_mode (DomainSecurityHeadersMode):
        response_header_timeout_secs (int):
        response_header_overrides (DomainResponseHeaderOverridesType0 | None): Header rewrites: `set` adds/overwrites,
            `remove` deletes. Null clears all.
        request_header_overrides (DomainRequestHeaderOverridesType0 | None): Header rewrites: `set` adds/overwrites,
            `remove` deletes. Null clears all.
        max_request_body_mb (int | None):
        response_compression (bool):
        ip_allow_list (list[str] | None):
        ip_deny_list (list[str] | None):
        basic_auth_user (None | str):
        basic_auth_enabled (bool):
        cors_config (DomainCorsConfigType0 | None):
        origin_scheme (DomainOriginScheme):
        proxy_protocol (DomainProxyProtocol):
        is_wildcard (bool):
        wildcard_cert_state (DomainWildcardCertState):
        acme_delegation_target (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    cube_id: str
    domain: str
    port: int | None
    status: str
    ingress_status: None | str
    security_headers_mode: DomainSecurityHeadersMode
    response_header_timeout_secs: int
    response_header_overrides: DomainResponseHeaderOverridesType0 | None
    request_header_overrides: DomainRequestHeaderOverridesType0 | None
    max_request_body_mb: int | None
    response_compression: bool
    ip_allow_list: list[str] | None
    ip_deny_list: list[str] | None
    basic_auth_user: None | str
    basic_auth_enabled: bool
    cors_config: DomainCorsConfigType0 | None
    origin_scheme: DomainOriginScheme
    proxy_protocol: DomainProxyProtocol
    is_wildcard: bool
    wildcard_cert_state: DomainWildcardCertState
    acme_delegation_target: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_cors_config_type_0 import DomainCorsConfigType0
        from ..models.domain_request_header_overrides_type_0 import (
            DomainRequestHeaderOverridesType0,
        )
        from ..models.domain_response_header_overrides_type_0 import (
            DomainResponseHeaderOverridesType0,
        )

        id = self.id

        cube_id = self.cube_id

        domain = self.domain

        port: int | None
        port = self.port

        status = self.status

        ingress_status: None | str
        ingress_status = self.ingress_status

        security_headers_mode = self.security_headers_mode.value

        response_header_timeout_secs = self.response_header_timeout_secs

        response_header_overrides: dict[str, Any] | None
        if isinstance(
            self.response_header_overrides, DomainResponseHeaderOverridesType0
        ):
            response_header_overrides = self.response_header_overrides.to_dict()
        else:
            response_header_overrides = self.response_header_overrides

        request_header_overrides: dict[str, Any] | None
        if isinstance(self.request_header_overrides, DomainRequestHeaderOverridesType0):
            request_header_overrides = self.request_header_overrides.to_dict()
        else:
            request_header_overrides = self.request_header_overrides

        max_request_body_mb: int | None
        max_request_body_mb = self.max_request_body_mb

        response_compression = self.response_compression

        ip_allow_list: list[str] | None
        if isinstance(self.ip_allow_list, list):
            ip_allow_list = self.ip_allow_list

        else:
            ip_allow_list = self.ip_allow_list

        ip_deny_list: list[str] | None
        if isinstance(self.ip_deny_list, list):
            ip_deny_list = self.ip_deny_list

        else:
            ip_deny_list = self.ip_deny_list

        basic_auth_user: None | str
        basic_auth_user = self.basic_auth_user

        basic_auth_enabled = self.basic_auth_enabled

        cors_config: dict[str, Any] | None
        if isinstance(self.cors_config, DomainCorsConfigType0):
            cors_config = self.cors_config.to_dict()
        else:
            cors_config = self.cors_config

        origin_scheme = self.origin_scheme.value

        proxy_protocol = self.proxy_protocol.value

        is_wildcard = self.is_wildcard

        wildcard_cert_state = self.wildcard_cert_state.value

        acme_delegation_target: None | str
        acme_delegation_target = self.acme_delegation_target

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "cubeId": cube_id,
                "domain": domain,
                "port": port,
                "status": status,
                "ingressStatus": ingress_status,
                "securityHeadersMode": security_headers_mode,
                "responseHeaderTimeoutSecs": response_header_timeout_secs,
                "responseHeaderOverrides": response_header_overrides,
                "requestHeaderOverrides": request_header_overrides,
                "maxRequestBodyMb": max_request_body_mb,
                "responseCompression": response_compression,
                "ipAllowList": ip_allow_list,
                "ipDenyList": ip_deny_list,
                "basicAuthUser": basic_auth_user,
                "basicAuthEnabled": basic_auth_enabled,
                "corsConfig": cors_config,
                "originScheme": origin_scheme,
                "proxyProtocol": proxy_protocol,
                "isWildcard": is_wildcard,
                "wildcardCertState": wildcard_cert_state,
                "acmeDelegationTarget": acme_delegation_target,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.domain_cors_config_type_0 import DomainCorsConfigType0
        from ..models.domain_request_header_overrides_type_0 import (
            DomainRequestHeaderOverridesType0,
        )
        from ..models.domain_response_header_overrides_type_0 import (
            DomainResponseHeaderOverridesType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        cube_id = d.pop("cubeId")

        domain = d.pop("domain")

        def _parse_port(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        port = _parse_port(d.pop("port"))

        status = d.pop("status")

        def _parse_ingress_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ingress_status = _parse_ingress_status(d.pop("ingressStatus"))

        security_headers_mode = DomainSecurityHeadersMode(d.pop("securityHeadersMode"))

        response_header_timeout_secs = d.pop("responseHeaderTimeoutSecs")

        def _parse_response_header_overrides(
            data: object,
        ) -> DomainResponseHeaderOverridesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_header_overrides_type_0 = (
                    DomainResponseHeaderOverridesType0.from_dict(data)
                )

                return response_header_overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainResponseHeaderOverridesType0 | None, data)

        response_header_overrides = _parse_response_header_overrides(
            d.pop("responseHeaderOverrides")
        )

        def _parse_request_header_overrides(
            data: object,
        ) -> DomainRequestHeaderOverridesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_header_overrides_type_0 = (
                    DomainRequestHeaderOverridesType0.from_dict(data)
                )

                return request_header_overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainRequestHeaderOverridesType0 | None, data)

        request_header_overrides = _parse_request_header_overrides(
            d.pop("requestHeaderOverrides")
        )

        def _parse_max_request_body_mb(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_request_body_mb = _parse_max_request_body_mb(d.pop("maxRequestBodyMb"))

        response_compression = d.pop("responseCompression")

        def _parse_ip_allow_list(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_allow_list_type_0 = cast(list[str], data)

                return ip_allow_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        ip_allow_list = _parse_ip_allow_list(d.pop("ipAllowList"))

        def _parse_ip_deny_list(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_deny_list_type_0 = cast(list[str], data)

                return ip_deny_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        ip_deny_list = _parse_ip_deny_list(d.pop("ipDenyList"))

        def _parse_basic_auth_user(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        basic_auth_user = _parse_basic_auth_user(d.pop("basicAuthUser"))

        basic_auth_enabled = d.pop("basicAuthEnabled")

        def _parse_cors_config(data: object) -> DomainCorsConfigType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cors_config_type_0 = DomainCorsConfigType0.from_dict(data)

                return cors_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainCorsConfigType0 | None, data)

        cors_config = _parse_cors_config(d.pop("corsConfig"))

        origin_scheme = DomainOriginScheme(d.pop("originScheme"))

        proxy_protocol = DomainProxyProtocol(d.pop("proxyProtocol"))

        is_wildcard = d.pop("isWildcard")

        wildcard_cert_state = DomainWildcardCertState(d.pop("wildcardCertState"))

        def _parse_acme_delegation_target(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acme_delegation_target = _parse_acme_delegation_target(
            d.pop("acmeDelegationTarget")
        )

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        domain = cls(
            id=id,
            cube_id=cube_id,
            domain=domain,
            port=port,
            status=status,
            ingress_status=ingress_status,
            security_headers_mode=security_headers_mode,
            response_header_timeout_secs=response_header_timeout_secs,
            response_header_overrides=response_header_overrides,
            request_header_overrides=request_header_overrides,
            max_request_body_mb=max_request_body_mb,
            response_compression=response_compression,
            ip_allow_list=ip_allow_list,
            ip_deny_list=ip_deny_list,
            basic_auth_user=basic_auth_user,
            basic_auth_enabled=basic_auth_enabled,
            cors_config=cors_config,
            origin_scheme=origin_scheme,
            proxy_protocol=proxy_protocol,
            is_wildcard=is_wildcard,
            wildcard_cert_state=wildcard_cert_state,
            acme_delegation_target=acme_delegation_target,
            created_at=created_at,
            updated_at=updated_at,
        )

        domain.additional_properties = d
        return domain

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
