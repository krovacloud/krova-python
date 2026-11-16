from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    space_id: str,
    endpoint_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/spaces/{space_id}/webhooks/{endpoint_id}".format(
            space_id=quote(str(space_id), safe=""),
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Error]:
    """Delete a webhook (cascades deliveries)

    Args:
        space_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        endpoint_id=endpoint_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | None:
    """Delete a webhook (cascades deliveries)

    Args:
        space_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        space_id=space_id,
        endpoint_id=endpoint_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Error]:
    """Delete a webhook (cascades deliveries)

    Args:
        space_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        endpoint_id=endpoint_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | None:
    """Delete a webhook (cascades deliveries)

    Args:
        space_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            endpoint_id=endpoint_id,
            client=client,
        )
    ).parsed
