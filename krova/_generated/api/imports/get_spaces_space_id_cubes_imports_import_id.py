from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_spaces_space_id_cubes_imports_import_id_response_200 import (
    GetSpacesSpaceIdCubesImportsImportIdResponse200,
)
from ...types import Response


def _get_kwargs(
    space_id: str,
    import_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/spaces/{space_id}/cubes/imports/{import_id}".format(
            space_id=quote(str(space_id), safe=""),
            import_id=quote(str(import_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetSpacesSpaceIdCubesImportsImportIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetSpacesSpaceIdCubesImportsImportIdResponse200.from_dict(
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
) -> Response[Error | GetSpacesSpaceIdCubesImportsImportIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: str,
    import_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetSpacesSpaceIdCubesImportsImportIdResponse200]:
    """Get the current state of an import

    Args:
        space_id (str):
        import_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSpacesSpaceIdCubesImportsImportIdResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        import_id=import_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: str,
    import_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetSpacesSpaceIdCubesImportsImportIdResponse200 | None:
    """Get the current state of an import

    Args:
        space_id (str):
        import_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSpacesSpaceIdCubesImportsImportIdResponse200
    """

    return sync_detailed(
        space_id=space_id,
        import_id=import_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    import_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetSpacesSpaceIdCubesImportsImportIdResponse200]:
    """Get the current state of an import

    Args:
        space_id (str):
        import_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSpacesSpaceIdCubesImportsImportIdResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        import_id=import_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    import_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetSpacesSpaceIdCubesImportsImportIdResponse200 | None:
    """Get the current state of an import

    Args:
        space_id (str):
        import_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSpacesSpaceIdCubesImportsImportIdResponse200
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            import_id=import_id,
            client=client,
        )
    ).parsed
