from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.patch_spaces_space_id_cubes_cube_id_domains_mapping_id_body import (
    PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody,
)
from ...models.patch_spaces_space_id_cubes_cube_id_domains_mapping_id_response_200 import (
    PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200,
)
from ...types import Response


def _get_kwargs(
    space_id: str,
    cube_id: str,
    mapping_id: str,
    *,
    body: PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/spaces/{space_id}/cubes/{cube_id}/domains/{mapping_id}".format(
            space_id=quote(str(space_id), safe=""),
            cube_id=quote(str(cube_id), safe=""),
            mapping_id=quote(str(mapping_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

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
) -> Response[Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: str,
    cube_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody,
) -> Response[Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200]:
    """Update a custom domain's proxy settings

     Partial update — only the fields you send change; omitted fields are left as-is. The Basic Auth
    password is write-only and bcrypt-hashed server-side.

    Args:
        space_id (str):
        cube_id (str):
        mapping_id (str):
        body (PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
        mapping_id=mapping_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: str,
    cube_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody,
) -> Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200 | None:
    """Update a custom domain's proxy settings

     Partial update — only the fields you send change; omitted fields are left as-is. The Basic Auth
    password is write-only and bcrypt-hashed server-side.

    Args:
        space_id (str):
        cube_id (str):
        mapping_id (str):
        body (PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200
    """

    return sync_detailed(
        space_id=space_id,
        cube_id=cube_id,
        mapping_id=mapping_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    cube_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody,
) -> Response[Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200]:
    """Update a custom domain's proxy settings

     Partial update — only the fields you send change; omitted fields are left as-is. The Basic Auth
    password is write-only and bcrypt-hashed server-side.

    Args:
        space_id (str):
        cube_id (str):
        mapping_id (str):
        body (PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
        mapping_id=mapping_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    cube_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody,
) -> Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200 | None:
    """Update a custom domain's proxy settings

     Partial update — only the fields you send change; omitted fields are left as-is. The Basic Auth
    password is write-only and bcrypt-hashed server-side.

    Args:
        space_id (str):
        cube_id (str):
        mapping_id (str):
        body (PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdResponse200
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            cube_id=cube_id,
            mapping_id=mapping_id,
            client=client,
            body=body,
        )
    ).parsed
