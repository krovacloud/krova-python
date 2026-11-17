from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.post_spaces_space_id_cubes_cube_id_snapshots_body import (
    PostSpacesSpaceIdCubesCubeIdSnapshotsBody,
)
from ...models.post_spaces_space_id_cubes_cube_id_snapshots_response_201 import (
    PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    space_id: str,
    cube_id: str,
    *,
    body: PostSpacesSpaceIdCubesCubeIdSnapshotsBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/spaces/{space_id}/cubes/{cube_id}/snapshots".format(
            space_id=quote(str(space_id), safe=""),
            cube_id=quote(str(cube_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201 | None:
    if response.status_code == 201:
        response_201 = PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201.from_dict(
            response.json()
        )

        return response_201

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: str,
    cube_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdCubesCubeIdSnapshotsBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201]:
    """Create a snapshot

    Args:
        space_id (str):
        cube_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdCubesCubeIdSnapshotsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: str,
    cube_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdCubesCubeIdSnapshotsBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201 | None:
    """Create a snapshot

    Args:
        space_id (str):
        cube_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdCubesCubeIdSnapshotsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201
    """

    return sync_detailed(
        space_id=space_id,
        cube_id=cube_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    cube_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdCubesCubeIdSnapshotsBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201]:
    """Create a snapshot

    Args:
        space_id (str):
        cube_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdCubesCubeIdSnapshotsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    cube_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdCubesCubeIdSnapshotsBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201 | None:
    """Create a snapshot

    Args:
        space_id (str):
        cube_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdCubesCubeIdSnapshotsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PostSpacesSpaceIdCubesCubeIdSnapshotsResponse201
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            cube_id=cube_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
