from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_spaces_space_id_cubes_cube_id_domains_mapping_id_records_response_200 import (
    GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200,
)
from ...types import Response


def _get_kwargs(
    space_id: str,
    cube_id: str,
    mapping_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/spaces/{space_id}/cubes/{cube_id}/domains/{mapping_id}/records".format(
            space_id=quote(str(space_id), safe=""),
            cube_id=quote(str(cube_id), safe=""),
            mapping_id=quote(str(mapping_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200 | None:
    if response.status_code == 200:
        response_200 = (
            GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200]:
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
) -> Response[Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200]:
    """DNS records this domain needs, with their live status

     Every record required for the domain to work, each checked against live DNS. Poll this after
    publishing them.

    `state` is per record: `found`, `missing` (not published yet — the expected state before you add it,
    never an error), `mismatch` (something else is there), or `unknown` (we could not check — never a
    statement about your DNS). `summary.complete` is true only when every record is `found`.

    A wildcard needs three records; an exact host needs one. Each call performs live DNS lookups and is
    rate limited.

    Args:
        space_id (str):
        cube_id (str):
        mapping_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
        mapping_id=mapping_id,
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
) -> Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200 | None:
    """DNS records this domain needs, with their live status

     Every record required for the domain to work, each checked against live DNS. Poll this after
    publishing them.

    `state` is per record: `found`, `missing` (not published yet — the expected state before you add it,
    never an error), `mismatch` (something else is there), or `unknown` (we could not check — never a
    statement about your DNS). `summary.complete` is true only when every record is `found`.

    A wildcard needs three records; an exact host needs one. Each call performs live DNS lookups and is
    rate limited.

    Args:
        space_id (str):
        cube_id (str):
        mapping_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200
    """

    return sync_detailed(
        space_id=space_id,
        cube_id=cube_id,
        mapping_id=mapping_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    cube_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200]:
    """DNS records this domain needs, with their live status

     Every record required for the domain to work, each checked against live DNS. Poll this after
    publishing them.

    `state` is per record: `found`, `missing` (not published yet — the expected state before you add it,
    never an error), `mismatch` (something else is there), or `unknown` (we could not check — never a
    statement about your DNS). `summary.complete` is true only when every record is `found`.

    A wildcard needs three records; an exact host needs one. Each call performs live DNS lookups and is
    rate limited.

    Args:
        space_id (str):
        cube_id (str):
        mapping_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
        mapping_id=mapping_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    cube_id: str,
    mapping_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200 | None:
    """DNS records this domain needs, with their live status

     Every record required for the domain to work, each checked against live DNS. Poll this after
    publishing them.

    `state` is per record: `found`, `missing` (not published yet — the expected state before you add it,
    never an error), `mismatch` (something else is there), or `unknown` (we could not check — never a
    statement about your DNS). `summary.complete` is true only when every record is `found`.

    A wildcard needs three records; an exact host needs one. Each call performs live DNS lookups and is
    rate limited.

    Args:
        space_id (str):
        cube_id (str):
        mapping_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetSpacesSpaceIdCubesCubeIdDomainsMappingIdRecordsResponse200
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            cube_id=cube_id,
            mapping_id=mapping_id,
            client=client,
        )
    ).parsed
