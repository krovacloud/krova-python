from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_spaces_space_id_cubes_imports_body import (
    PostSpacesSpaceIdCubesImportsBody,
)
from ...models.post_spaces_space_id_cubes_imports_response_201 import (
    PostSpacesSpaceIdCubesImportsResponse201,
)
from ...types import Response


def _get_kwargs(
    space_id: str,
    *,
    body: PostSpacesSpaceIdCubesImportsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/spaces/{space_id}/cubes/imports".format(
            space_id=quote(str(space_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostSpacesSpaceIdCubesImportsResponse201 | None:
    if response.status_code == 201:
        response_201 = PostSpacesSpaceIdCubesImportsResponse201.from_dict(
            response.json()
        )

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostSpacesSpaceIdCubesImportsResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdCubesImportsBody,
) -> Response[Any | PostSpacesSpaceIdCubesImportsResponse201]:
    """Initiate a .cube archive import (browser-side multipart upload)

    Args:
        space_id (str):
        body (PostSpacesSpaceIdCubesImportsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSpacesSpaceIdCubesImportsResponse201]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdCubesImportsBody,
) -> Any | PostSpacesSpaceIdCubesImportsResponse201 | None:
    """Initiate a .cube archive import (browser-side multipart upload)

    Args:
        space_id (str):
        body (PostSpacesSpaceIdCubesImportsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSpacesSpaceIdCubesImportsResponse201
    """

    return sync_detailed(
        space_id=space_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdCubesImportsBody,
) -> Response[Any | PostSpacesSpaceIdCubesImportsResponse201]:
    """Initiate a .cube archive import (browser-side multipart upload)

    Args:
        space_id (str):
        body (PostSpacesSpaceIdCubesImportsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSpacesSpaceIdCubesImportsResponse201]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSpacesSpaceIdCubesImportsBody,
) -> Any | PostSpacesSpaceIdCubesImportsResponse201 | None:
    """Initiate a .cube archive import (browser-side multipart upload)

    Args:
        space_id (str):
        body (PostSpacesSpaceIdCubesImportsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSpacesSpaceIdCubesImportsResponse201
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            client=client,
            body=body,
        )
    ).parsed
