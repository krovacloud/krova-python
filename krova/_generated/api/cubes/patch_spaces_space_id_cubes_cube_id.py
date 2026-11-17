from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.patch_spaces_space_id_cubes_cube_id_body import (
    PatchSpacesSpaceIdCubesCubeIdBody,
)
from ...models.patch_spaces_space_id_cubes_cube_id_response_200 import (
    PatchSpacesSpaceIdCubesCubeIdResponse200,
)
from ...types import Response


def _get_kwargs(
    space_id: str,
    cube_id: str,
    *,
    body: PatchSpacesSpaceIdCubesCubeIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/spaces/{space_id}/cubes/{cube_id}".format(
            space_id=quote(str(space_id), safe=""),
            cube_id=quote(str(cube_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PatchSpacesSpaceIdCubesCubeIdResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchSpacesSpaceIdCubesCubeIdResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

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
) -> Response[Error | PatchSpacesSpaceIdCubesCubeIdResponse200]:
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
    body: PatchSpacesSpaceIdCubesCubeIdBody,
) -> Response[Error | PatchSpacesSpaceIdCubesCubeIdResponse200]:
    """Update a Cube (rename, termination protection, idle auto-stop)

     Idempotent. The PATCHable fields are `name`, `terminationProtection` and `idleTimeoutMinutes`; send
    any combination. Sending a value a field already has returns the Cube unchanged and writes no audit
    row. Sending none of them is a 400 rather than a no-op, so a typo in a field name cannot look like
    success. Renaming and changing the idle auto-stop timeout need the `cube.manage` permission and
    changing termination protection needs `cube.termination_protection`; a request with several fields
    needs every matching permission. Every supplied field is validated before any is applied. Names are
    not unique within a space. Renaming is metadata only: the hostname inside a running Cube changes on
    its next cold restart. To change vCPU, RAM or disk use `POST .../resize`.

    Args:
        space_id (str):
        cube_id (str):
        body (PatchSpacesSpaceIdCubesCubeIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PatchSpacesSpaceIdCubesCubeIdResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
        body=body,
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
    body: PatchSpacesSpaceIdCubesCubeIdBody,
) -> Error | PatchSpacesSpaceIdCubesCubeIdResponse200 | None:
    """Update a Cube (rename, termination protection, idle auto-stop)

     Idempotent. The PATCHable fields are `name`, `terminationProtection` and `idleTimeoutMinutes`; send
    any combination. Sending a value a field already has returns the Cube unchanged and writes no audit
    row. Sending none of them is a 400 rather than a no-op, so a typo in a field name cannot look like
    success. Renaming and changing the idle auto-stop timeout need the `cube.manage` permission and
    changing termination protection needs `cube.termination_protection`; a request with several fields
    needs every matching permission. Every supplied field is validated before any is applied. Names are
    not unique within a space. Renaming is metadata only: the hostname inside a running Cube changes on
    its next cold restart. To change vCPU, RAM or disk use `POST .../resize`.

    Args:
        space_id (str):
        cube_id (str):
        body (PatchSpacesSpaceIdCubesCubeIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PatchSpacesSpaceIdCubesCubeIdResponse200
    """

    return sync_detailed(
        space_id=space_id,
        cube_id=cube_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    space_id: str,
    cube_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchSpacesSpaceIdCubesCubeIdBody,
) -> Response[Error | PatchSpacesSpaceIdCubesCubeIdResponse200]:
    """Update a Cube (rename, termination protection, idle auto-stop)

     Idempotent. The PATCHable fields are `name`, `terminationProtection` and `idleTimeoutMinutes`; send
    any combination. Sending a value a field already has returns the Cube unchanged and writes no audit
    row. Sending none of them is a 400 rather than a no-op, so a typo in a field name cannot look like
    success. Renaming and changing the idle auto-stop timeout need the `cube.manage` permission and
    changing termination protection needs `cube.termination_protection`; a request with several fields
    needs every matching permission. Every supplied field is validated before any is applied. Names are
    not unique within a space. Renaming is metadata only: the hostname inside a running Cube changes on
    its next cold restart. To change vCPU, RAM or disk use `POST .../resize`.

    Args:
        space_id (str):
        cube_id (str):
        body (PatchSpacesSpaceIdCubesCubeIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PatchSpacesSpaceIdCubesCubeIdResponse200]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        cube_id=cube_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: str,
    cube_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchSpacesSpaceIdCubesCubeIdBody,
) -> Error | PatchSpacesSpaceIdCubesCubeIdResponse200 | None:
    """Update a Cube (rename, termination protection, idle auto-stop)

     Idempotent. The PATCHable fields are `name`, `terminationProtection` and `idleTimeoutMinutes`; send
    any combination. Sending a value a field already has returns the Cube unchanged and writes no audit
    row. Sending none of them is a 400 rather than a no-op, so a typo in a field name cannot look like
    success. Renaming and changing the idle auto-stop timeout need the `cube.manage` permission and
    changing termination protection needs `cube.termination_protection`; a request with several fields
    needs every matching permission. Every supplied field is validated before any is applied. Names are
    not unique within a space. Renaming is metadata only: the hostname inside a running Cube changes on
    its next cold restart. To change vCPU, RAM or disk use `POST .../resize`.

    Args:
        space_id (str):
        cube_id (str):
        body (PatchSpacesSpaceIdCubesCubeIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PatchSpacesSpaceIdCubesCubeIdResponse200
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            cube_id=cube_id,
            client=client,
            body=body,
        )
    ).parsed
