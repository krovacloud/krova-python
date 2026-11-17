from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    space_id: str,
    cube_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/spaces/{space_id}/cubes/{cube_id}/restart".format(
            space_id=quote(str(space_id), safe=""),
            cube_id=quote(str(cube_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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
) -> Response[Any | Error]:
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
) -> Response[Any | Error]:
    """Restart a running Cube

     Cold-restarts the Cube: the hypervisor process is stopped and relaunched, so the Cube boots against
    the host's current kernel. This is how a Cube picks up a refreshed guest kernel after a platform
    image update — a `reboot` issued inside the Cube cannot do it, because the kernel is supplied
    externally by the host. Disk state is preserved; only the kernel changes. Cube must be `running` (a
    stopped Cube already picks up the latest kernel when started). Concurrent restarts of the same Cube
    are rejected with 409 rather than queued twice.

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
) -> Any | Error | None:
    """Restart a running Cube

     Cold-restarts the Cube: the hypervisor process is stopped and relaunched, so the Cube boots against
    the host's current kernel. This is how a Cube picks up a refreshed guest kernel after a platform
    image update — a `reboot` issued inside the Cube cannot do it, because the kernel is supplied
    externally by the host. Disk state is preserved; only the kernel changes. Cube must be `running` (a
    stopped Cube already picks up the latest kernel when started). Concurrent restarts of the same Cube
    are rejected with 409 rather than queued twice.

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
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
) -> Response[Any | Error]:
    """Restart a running Cube

     Cold-restarts the Cube: the hypervisor process is stopped and relaunched, so the Cube boots against
    the host's current kernel. This is how a Cube picks up a refreshed guest kernel after a platform
    image update — a `reboot` issued inside the Cube cannot do it, because the kernel is supplied
    externally by the host. Disk state is preserved; only the kernel changes. Cube must be `running` (a
    stopped Cube already picks up the latest kernel when started). Concurrent restarts of the same Cube
    are rejected with 409 rather than queued twice.

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
) -> Any | Error | None:
    """Restart a running Cube

     Cold-restarts the Cube: the hypervisor process is stopped and relaunched, so the Cube boots against
    the host's current kernel. This is how a Cube picks up a refreshed guest kernel after a platform
    image update — a `reboot` issued inside the Cube cannot do it, because the kernel is supplied
    externally by the host. Disk state is preserved; only the kernel changes. Cube must be `running` (a
    stopped Cube already picks up the latest kernel when started). Concurrent restarts of the same Cube
    are rejected with 409 rather than queued twice.

    Args:
        space_id (str):
        cube_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            cube_id=cube_id,
            client=client,
        )
    ).parsed
