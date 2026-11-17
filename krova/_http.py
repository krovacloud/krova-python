"""The one place the SDK touches the generated client."""

from __future__ import annotations

from typing import Any, Protocol

import httpx

from ._generated.client import AuthenticatedClient
from .errors import error_from_response

API_PATH = "/api/v1"


class Operation(Protocol):
    """A generated ``krova._generated.api.*`` module: all we use is its request builder."""

    def _get_kwargs(self, *args: Any, **kwargs: Any) -> dict[str, Any]: ...


def api_url(base_url: str) -> str:
    """Add ``/api/v1`` to a site origin; a URL that already ends in it passes through."""
    base = base_url.rstrip("/")
    return base if base.endswith(API_PATH) else base + API_PATH


class Transport:
    """Sends the requests the generated modules describe and turns failures into ``KrovaError``.

    The generated ``sync_detailed`` helpers parse the response before we can see it, and break on
    error bodies the spec does not describe. So we use only the generated request builders and
    models, and own the status check ourselves.
    """

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        timeout: float,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        httpx_args: dict[str, Any] = {}
        if transport is not None:
            httpx_args["transport"] = transport
        self._client = AuthenticatedClient(
            base_url=api_url(base_url),
            token=api_key,
            prefix="",
            auth_header_name="X-API-KEY",
            timeout=httpx.Timeout(timeout),
            httpx_args=httpx_args,
        )

    def call(self, operation: Operation, *args: Any, **kwargs: Any) -> httpx.Response:
        request = operation._get_kwargs(*args, **kwargs)
        response = self._client.get_httpx_client().request(**request)
        if not response.is_success:
            raise error_from_response(response)
        return response

    def close(self) -> None:
        self._client.get_httpx_client().close()
