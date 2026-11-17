from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_spaces_space_id_backups_backup_id_response_200 import (
    GetSpacesSpaceIdBackupsBackupIdResponse200,
)
from ...types import Response


def _get_kwargs(
    space_id: str,
    backup_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/spaces/{space_id}/backups/{backup_id}".format(
            space_id=quote(str(space_id), safe=""),
            backup_id=quote(str(backup_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetSpacesSpaceIdBackupsBackupIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSpacesSpaceIdBackupsBackupIdResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetSpacesSpaceIdBackupsBackupIdResponse200]:
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
) -> Response[Error | GetSpacesSpaceIdBackupsBackupIdResponse200]:
    """Get one backup

    Args:
        space_id (str):
        backup_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSpacesSpaceIdBackupsBackupIdResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        backup_id=backup_id,
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
) -> Error | GetSpacesSpaceIdBackupsBackupIdResponse200 | None:
    """Get one backup

    Args:
        space_id (str):
        backup_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSpacesSpaceIdBackupsBackupIdResponse200
    """

    return sync_detailed(
        space_id=space_id,
        backup_id=backup_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    backup_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetSpacesSpaceIdBackupsBackupIdResponse200]:
    """Get one backup

    Args:
        space_id (str):
        backup_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSpacesSpaceIdBackupsBackupIdResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        backup_id=backup_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    backup_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetSpacesSpaceIdBackupsBackupIdResponse200 | None:
    """Get one backup

    Args:
        space_id (str):
        backup_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSpacesSpaceIdBackupsBackupIdResponse200
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            backup_id=backup_id,
            client=client,
        )
    ).parsed
