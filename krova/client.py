"""The ``Krova`` client."""

from __future__ import annotations

import os
from types import TracebackType

import httpx

from ._http import Transport
from .cubes import Cubes

DEFAULT_BASE_URL = "https://krova.cloud"


class Krova:
    """Client for the Krova Cloud API, scoped to one Space.

    ``api_key`` and ``space_id`` fall back to the ``KROVA_API_KEY`` and ``KROVA_SPACE_ID``
    environment variables, the same ones the Krova CLI reads. ``base_url`` is the site origin;
    ``/api/v1`` is added for you. ``transport`` replaces the HTTP transport, which is how the
    tests run without a network.

    Resources hang off the client (``client.cubes``). Command execution and file transfer will
    be added later as ``client.run`` and ``client.files`` style modules next to ``cubes``.
    """

    cubes: Cubes

    def __init__(
        self,
        api_key: str | None = None,
        space_id: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        resolved_key = api_key or os.environ.get("KROVA_API_KEY")
        resolved_space = space_id or os.environ.get("KROVA_SPACE_ID")
        if not resolved_key:
            raise ValueError("No API key: pass api_key or set KROVA_API_KEY")
        if not resolved_space:
            raise ValueError("No Space: pass space_id or set KROVA_SPACE_ID")
        self.space_id = resolved_space
        self._transport = Transport(
            api_key=resolved_key, base_url=base_url, timeout=timeout, transport=transport
        )
        self.cubes = Cubes(self._transport, resolved_space)

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> Krova:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()
