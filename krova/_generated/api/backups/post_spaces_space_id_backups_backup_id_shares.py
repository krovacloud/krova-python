from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.post_spaces_space_id_backups_backup_id_shares_body import (
    PostSpacesSpaceIdBackupsBackupIdSharesBody,
)
from ...models.post_spaces_space_id_backups_backup_id_shares_response_201 import (
    PostSpacesSpaceIdBackupsBackupIdSharesResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    space_id: str,
    backup_id: str,
    *,
    body: PostSpacesSpaceIdBackupsBackupIdSharesBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/spaces/{space_id}/backups/{backup_id}/shares".format(
            space_id=quote(str(space_id), safe=""),
            backup_id=quote(str(backup_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201 | None:
    if response.status_code == 201:
        response_201 = PostSpacesSpaceIdBackupsBackupIdSharesResponse201.from_dict(
            response.json()
        )

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

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
) -> Response[Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: str,
    backup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdBackupsBackupIdSharesBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201]:
    """Offer a copy of this backup to another space

     Requires `backup.manage`. Creates a pending share request that the destination space accepts within
    48 hours: its owner, or a member there with `backup.manage`, in the dashboard or with an API key of
    their own. On acceptance the destination gets its own copy of the backup and pays backup storage for
    it from that moment; this space's backup is unchanged. A request made with an API key never
    completes immediately, even when the key's user owns both spaces.

    Args:
        space_id (str):
        backup_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdBackupsBackupIdSharesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        backup_id=backup_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: str,
    backup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdBackupsBackupIdSharesBody,
    idempotency_key: str | Unset = UNSET,
) -> Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201 | None:
    """Offer a copy of this backup to another space

     Requires `backup.manage`. Creates a pending share request that the destination space accepts within
    48 hours: its owner, or a member there with `backup.manage`, in the dashboard or with an API key of
    their own. On acceptance the destination gets its own copy of the backup and pays backup storage for
    it from that moment; this space's backup is unchanged. A request made with an API key never
    completes immediately, even when the key's user owns both spaces.

    Args:
        space_id (str):
        backup_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdBackupsBackupIdSharesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201
    """

    return sync_detailed(
        space_id=space_id,
        backup_id=backup_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    backup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdBackupsBackupIdSharesBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201]:
    """Offer a copy of this backup to another space

     Requires `backup.manage`. Creates a pending share request that the destination space accepts within
    48 hours: its owner, or a member there with `backup.manage`, in the dashboard or with an API key of
    their own. On acceptance the destination gets its own copy of the backup and pays backup storage for
    it from that moment; this space's backup is unchanged. A request made with an API key never
    completes immediately, even when the key's user owns both spaces.

    Args:
        space_id (str):
        backup_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdBackupsBackupIdSharesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        backup_id=backup_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    backup_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdBackupsBackupIdSharesBody,
    idempotency_key: str | Unset = UNSET,
) -> Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201 | None:
    """Offer a copy of this backup to another space

     Requires `backup.manage`. Creates a pending share request that the destination space accepts within
    48 hours: its owner, or a member there with `backup.manage`, in the dashboard or with an API key of
    their own. On acceptance the destination gets its own copy of the backup and pays backup storage for
    it from that moment; this space's backup is unchanged. A request made with an API key never
    completes immediately, even when the key's user owns both spaces.

    Args:
        space_id (str):
        backup_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdBackupsBackupIdSharesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PostSpacesSpaceIdBackupsBackupIdSharesResponse201
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            backup_id=backup_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
