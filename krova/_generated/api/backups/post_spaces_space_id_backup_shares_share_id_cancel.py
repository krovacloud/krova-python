from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.post_spaces_space_id_backup_shares_share_id_cancel_response_200 import (
    PostSpacesSpaceIdBackupSharesShareIdCancelResponse200,
)
from ...types import Response


def _get_kwargs(
    space_id: str,
    share_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/spaces/{space_id}/backup-shares/{share_id}/cancel".format(
            space_id=quote(str(space_id), safe=""),
            share_id=quote(str(share_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200 | None:
    if response.status_code == 200:
        response_200 = PostSpacesSpaceIdBackupSharesShareIdCancelResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200]:
    """Withdraw a pending backup share offered by this space

     Allowed for an API key of this space's owner, of a member with `backup.manage`, or of the member who
    raised the request.

    Args:
        space_id (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        share_id=share_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200 | None:
    """Withdraw a pending backup share offered by this space

     Allowed for an API key of this space's owner, of a member with `backup.manage`, or of the member who
    raised the request.

    Args:
        space_id (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200
    """

    return sync_detailed(
        space_id=space_id,
        share_id=share_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200]:
    """Withdraw a pending backup share offered by this space

     Allowed for an API key of this space's owner, of a member with `backup.manage`, or of the member who
    raised the request.

    Args:
        space_id (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        share_id=share_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200 | None:
    """Withdraw a pending backup share offered by this space

     Allowed for an API key of this space's owner, of a member with `backup.manage`, or of the member who
    raised the request.

    Args:
        space_id (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PostSpacesSpaceIdBackupSharesShareIdCancelResponse200
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            share_id=share_id,
            client=client,
        )
    ).parsed
