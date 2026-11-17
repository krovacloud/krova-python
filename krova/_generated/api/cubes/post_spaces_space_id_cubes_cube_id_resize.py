from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.post_spaces_space_id_cubes_cube_id_resize_body import (
    PostSpacesSpaceIdCubesCubeIdResizeBody,
)
from ...models.post_spaces_space_id_cubes_cube_id_resize_response_200 import (
    PostSpacesSpaceIdCubesCubeIdResizeResponse200,
)
from ...models.post_spaces_space_id_cubes_cube_id_resize_response_400 import (
    PostSpacesSpaceIdCubesCubeIdResizeResponse400,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    space_id: str,
    cube_id: str,
    *,
    body: PostSpacesSpaceIdCubesCubeIdResizeBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/spaces/{space_id}/cubes/{cube_id}/resize".format(
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
) -> (
    Any
    | Error
    | PostSpacesSpaceIdCubesCubeIdResizeResponse200
    | PostSpacesSpaceIdCubesCubeIdResizeResponse400
    | None
):
    if response.status_code == 200:
        response_200 = PostSpacesSpaceIdCubesCubeIdResizeResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = PostSpacesSpaceIdCubesCubeIdResizeResponse400.from_dict(
            response.json()
        )

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

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
) -> Response[
    Any
    | Error
    | PostSpacesSpaceIdCubesCubeIdResizeResponse200
    | PostSpacesSpaceIdCubesCubeIdResizeResponse400
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
    body: PostSpacesSpaceIdCubesCubeIdResizeBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    Any
    | Error
    | PostSpacesSpaceIdCubesCubeIdResizeResponse200
    | PostSpacesSpaceIdCubesCubeIdResizeResponse400
]:
    r"""Resize a Cube (asynchronous)

     Changes a Cube's vCPU, RAM and/or disk. Send only the dimensions you want to change; the rest keep
    their current value. It goes through the same checks as the dashboard: the hardware ranges, your
    plan's per-Cube size limit (including any override on your space) and the free capacity of the host
    the Cube runs on. Disk can only grow. The Cube must be `running` or `stopped`. The response says
    whether the resize is `isLive` (RAM or disk growth, and vCPU changes on Cubes that support it,
    applied with no restart) or `requiresRestart` (a RAM shrink or a vCPU change on a Cube that cannot
    hotplug: the Cube is restarted to apply it). The change is applied by a background job, so the Cube
    keeps its current size until `GET` shows the new one. A second request while one is queued for the
    same Cube is rejected with 409. When the host itself has no room for the requested size the 400
    carries `code: \"insufficient_host_capacity\"` and the `dimension` that ran out.

    Args:
        space_id (str):
        cube_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdCubesCubeIdResizeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PostSpacesSpaceIdCubesCubeIdResizeResponse200 | PostSpacesSpaceIdCubesCubeIdResizeResponse400]
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
    body: PostSpacesSpaceIdCubesCubeIdResizeBody,
    idempotency_key: str | Unset = UNSET,
) -> (
    Any
    | Error
    | PostSpacesSpaceIdCubesCubeIdResizeResponse200
    | PostSpacesSpaceIdCubesCubeIdResizeResponse400
    | None
):
    r"""Resize a Cube (asynchronous)

     Changes a Cube's vCPU, RAM and/or disk. Send only the dimensions you want to change; the rest keep
    their current value. It goes through the same checks as the dashboard: the hardware ranges, your
    plan's per-Cube size limit (including any override on your space) and the free capacity of the host
    the Cube runs on. Disk can only grow. The Cube must be `running` or `stopped`. The response says
    whether the resize is `isLive` (RAM or disk growth, and vCPU changes on Cubes that support it,
    applied with no restart) or `requiresRestart` (a RAM shrink or a vCPU change on a Cube that cannot
    hotplug: the Cube is restarted to apply it). The change is applied by a background job, so the Cube
    keeps its current size until `GET` shows the new one. A second request while one is queued for the
    same Cube is rejected with 409. When the host itself has no room for the requested size the 400
    carries `code: \"insufficient_host_capacity\"` and the `dimension` that ran out.

    Args:
        space_id (str):
        cube_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdCubesCubeIdResizeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PostSpacesSpaceIdCubesCubeIdResizeResponse200 | PostSpacesSpaceIdCubesCubeIdResizeResponse400
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
    body: PostSpacesSpaceIdCubesCubeIdResizeBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    Any
    | Error
    | PostSpacesSpaceIdCubesCubeIdResizeResponse200
    | PostSpacesSpaceIdCubesCubeIdResizeResponse400
]:
    r"""Resize a Cube (asynchronous)

     Changes a Cube's vCPU, RAM and/or disk. Send only the dimensions you want to change; the rest keep
    their current value. It goes through the same checks as the dashboard: the hardware ranges, your
    plan's per-Cube size limit (including any override on your space) and the free capacity of the host
    the Cube runs on. Disk can only grow. The Cube must be `running` or `stopped`. The response says
    whether the resize is `isLive` (RAM or disk growth, and vCPU changes on Cubes that support it,
    applied with no restart) or `requiresRestart` (a RAM shrink or a vCPU change on a Cube that cannot
    hotplug: the Cube is restarted to apply it). The change is applied by a background job, so the Cube
    keeps its current size until `GET` shows the new one. A second request while one is queued for the
    same Cube is rejected with 409. When the host itself has no room for the requested size the 400
    carries `code: \"insufficient_host_capacity\"` and the `dimension` that ran out.

    Args:
        space_id (str):
        cube_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdCubesCubeIdResizeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PostSpacesSpaceIdCubesCubeIdResizeResponse200 | PostSpacesSpaceIdCubesCubeIdResizeResponse400]
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
    body: PostSpacesSpaceIdCubesCubeIdResizeBody,
    idempotency_key: str | Unset = UNSET,
) -> (
    Any
    | Error
    | PostSpacesSpaceIdCubesCubeIdResizeResponse200
    | PostSpacesSpaceIdCubesCubeIdResizeResponse400
    | None
):
    r"""Resize a Cube (asynchronous)

     Changes a Cube's vCPU, RAM and/or disk. Send only the dimensions you want to change; the rest keep
    their current value. It goes through the same checks as the dashboard: the hardware ranges, your
    plan's per-Cube size limit (including any override on your space) and the free capacity of the host
    the Cube runs on. Disk can only grow. The Cube must be `running` or `stopped`. The response says
    whether the resize is `isLive` (RAM or disk growth, and vCPU changes on Cubes that support it,
    applied with no restart) or `requiresRestart` (a RAM shrink or a vCPU change on a Cube that cannot
    hotplug: the Cube is restarted to apply it). The change is applied by a background job, so the Cube
    keeps its current size until `GET` shows the new one. A second request while one is queued for the
    same Cube is rejected with 409. When the host itself has no room for the requested size the 400
    carries `code: \"insufficient_host_capacity\"` and the `dimension` that ran out.

    Args:
        space_id (str):
        cube_id (str):
        idempotency_key (str | Unset):
        body (PostSpacesSpaceIdCubesCubeIdResizeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PostSpacesSpaceIdCubesCubeIdResizeResponse200 | PostSpacesSpaceIdCubesCubeIdResizeResponse400
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
