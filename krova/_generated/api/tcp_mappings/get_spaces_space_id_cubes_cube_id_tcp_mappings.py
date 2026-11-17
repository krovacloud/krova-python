from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_spaces_space_id_cubes_cube_id_tcp_mappings_response_200 import (
    GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200,
)
from ...types import Response


def _get_kwargs(
    space_id: str,
    cube_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/spaces/{space_id}/cubes/{cube_id}/tcp-mappings".format(
            space_id=quote(str(space_id), safe=""),
            cube_id=quote(str(cube_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200]:
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
) -> Response[GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200]:
    """List TCP port forwards for a Cube

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200]
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
) -> GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200 | None:
    """List TCP port forwards for a Cube

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200
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
) -> Response[GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200]:
    """List TCP port forwards for a Cube

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200]
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
) -> GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200 | None:
    """List TCP port forwards for a Cube

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSpacesSpaceIdCubesCubeIdTcpMappingsResponse200
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            cube_id=cube_id,
            client=client,
        )
    ).parsed
