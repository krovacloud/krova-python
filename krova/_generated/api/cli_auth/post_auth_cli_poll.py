from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.post_auth_cli_poll_body import PostAuthCliPollBody
from ...models.post_auth_cli_poll_response_200 import PostAuthCliPollResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostAuthCliPollBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/cli/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | PostAuthCliPollResponse200 | None:
    if response.status_code == 200:
        response_200 = PostAuthCliPollResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 410:
        response_410 = cast(Any, None)
        return response_410

    if response.status_code == 428:
        response_428 = cast(Any, None)
        return response_428

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | PostAuthCliPollResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostAuthCliPollBody,
) -> Response[Any | Error | PostAuthCliPollResponse200]:
    """Poll for CLI device-authorization approval (RFC 8628)

     Public, unauthenticated. The CLI submits its deviceCode until the user approves or denies. On
    approval a real API key is minted ONCE, scoped to the approved Space and the approving user's
    membership, and returned a single time. Rate-limited per client IP.

    Args:
        body (PostAuthCliPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PostAuthCliPollResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostAuthCliPollBody,
) -> Any | Error | PostAuthCliPollResponse200 | None:
    """Poll for CLI device-authorization approval (RFC 8628)

     Public, unauthenticated. The CLI submits its deviceCode until the user approves or denies. On
    approval a real API key is minted ONCE, scoped to the approved Space and the approving user's
    membership, and returned a single time. Rate-limited per client IP.

    Args:
        body (PostAuthCliPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PostAuthCliPollResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostAuthCliPollBody,
) -> Response[Any | Error | PostAuthCliPollResponse200]:
    """Poll for CLI device-authorization approval (RFC 8628)

     Public, unauthenticated. The CLI submits its deviceCode until the user approves or denies. On
    approval a real API key is minted ONCE, scoped to the approved Space and the approving user's
    membership, and returned a single time. Rate-limited per client IP.

    Args:
        body (PostAuthCliPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PostAuthCliPollResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostAuthCliPollBody,
) -> Any | Error | PostAuthCliPollResponse200 | None:
    """Poll for CLI device-authorization approval (RFC 8628)

     Public, unauthenticated. The CLI submits its deviceCode until the user approves or denies. On
    approval a real API key is minted ONCE, scoped to the approved Space and the approving user's
    membership, and returned a single time. Rate-limited per client IP.

    Args:
        body (PostAuthCliPollBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PostAuthCliPollResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
