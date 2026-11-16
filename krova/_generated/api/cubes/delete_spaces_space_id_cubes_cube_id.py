from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_spaces_space_id_cubes_cube_id_response_200 import (
    DeleteSpacesSpaceIdCubesCubeIdResponse200,
)
from ...models.delete_spaces_space_id_cubes_cube_id_response_409 import (
    DeleteSpacesSpaceIdCubesCubeIdResponse409,
)
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    space_id: str,
    cube_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/spaces/{space_id}/cubes/{cube_id}".format(
            space_id=quote(str(space_id), safe=""),
            cube_id=quote(str(cube_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteSpacesSpaceIdCubesCubeIdResponse200
    | DeleteSpacesSpaceIdCubesCubeIdResponse409
    | Error
    | None
):
    if response.status_code == 200:
        response_200 = DeleteSpacesSpaceIdCubesCubeIdResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DeleteSpacesSpaceIdCubesCubeIdResponse409.from_dict(
            response.json()
        )

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
) -> Response[
    DeleteSpacesSpaceIdCubesCubeIdResponse200
    | DeleteSpacesSpaceIdCubesCubeIdResponse409
    | Error
]:
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
) -> Response[
    DeleteSpacesSpaceIdCubesCubeIdResponse200
    | DeleteSpacesSpaceIdCubesCubeIdResponse409
    | Error
]:
    """Delete a Cube (asynchronous)

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSpacesSpaceIdCubesCubeIdResponse200 | DeleteSpacesSpaceIdCubesCubeIdResponse409 | Error]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
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
) -> (
    DeleteSpacesSpaceIdCubesCubeIdResponse200
    | DeleteSpacesSpaceIdCubesCubeIdResponse409
    | Error
    | None
):
    """Delete a Cube (asynchronous)

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSpacesSpaceIdCubesCubeIdResponse200 | DeleteSpacesSpaceIdCubesCubeIdResponse409 | Error
    """

    return sync_detailed(
        space_id=space_id,
        cube_id=cube_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    cube_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteSpacesSpaceIdCubesCubeIdResponse200
    | DeleteSpacesSpaceIdCubesCubeIdResponse409
    | Error
]:
    """Delete a Cube (asynchronous)

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSpacesSpaceIdCubesCubeIdResponse200 | DeleteSpacesSpaceIdCubesCubeIdResponse409 | Error]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    cube_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteSpacesSpaceIdCubesCubeIdResponse200
    | DeleteSpacesSpaceIdCubesCubeIdResponse409
    | Error
    | None
):
    """Delete a Cube (asynchronous)

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSpacesSpaceIdCubesCubeIdResponse200 | DeleteSpacesSpaceIdCubesCubeIdResponse409 | Error
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            cube_id=cube_id,
            client=client,
        )
    ).parsed
