# krova-python

Python SDK for the Krova Cloud API. Early version: create, get, list and delete Cubes, power one off, read its SSH details, and wait until it is running. Not published to PyPI yet. Running commands and moving files are not part of this version.

## Install

Python 3.11 or newer.

```bash
pip install "git+https://github.com/krovacloud/krova-python.git"
```

## Quickstart

Create an API key in your Space and export it with the Space id.

```bash
export KROVA_API_KEY=kro_...
export KROVA_SPACE_ID=...
```

```python
from krova import Krova

with Krova() as krova:
    cube = krova.cubes.create(
        name="agent-box",
        image="ubuntu-24.04",  # placeholder: use an id from GET /api/v1/images
        vcpu=2,
        ram_gb=4,
        disk_gb=40,
        ssh_public_key=open("id_ed25519.pub").read().strip(),
    )
    cube.wait_until_running(timeout=300)

    ssh = cube.ssh()
    print(f"ssh {ssh.user}@{ssh.host} -p {ssh.port}")

    cube.delete()
```

`Krova(api_key=None, space_id=None, base_url="https://krova.cloud")` falls back to `KROVA_API_KEY` and `KROVA_SPACE_ID`. `image` is an id from the `/images` catalog; `ubuntu-24.04` above is a placeholder.

Other calls: `krova.cubes.get(id)`, `krova.cubes.list()`, `krova.cubes.delete(id)`, `krova.cubes.power_off(id)`, `krova.cubes.ssh(id)`.

## Errors

A failed call raises `krova.KrovaError` with `status`, `code`, `message` and `request_id`. Quote the request id when you contact support. Deleting a Cube with termination protection raises it with status 409 and code `termination_protected`. `wait_until_running` raises `WaitTimeoutError` on timeout and `CubeFailedError` if the Cube ends up in `error`, `deleted`, `stopped` or `stopping`; both are `KrovaError` subclasses.

## Development

```bash
uv sync
uv run ruff check .
uv run pytest
```

The HTTP layer in `krova/_generated/` is generated from `openapi.json` with a pinned `openapi-python-client`. Do not edit it by hand. To refresh it:

```bash
curl -fsSL https://krova.cloud/api/v1/openapi.json -o openapi.json
scripts/generate.sh
```

The hand-written API is `krova/client.py`, `krova/cubes.py` and `krova/errors.py`.
