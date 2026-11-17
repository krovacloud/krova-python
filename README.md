# krova-python

The Python SDK for [Krova Cloud](https://krova.cloud). Create and manage Cubes, run commands in them and move files, from your own code or from an AI agent.

- Cubes: create, get, list, rename, resize, set idle auto-stop, delete, power off, read SSH details and wait until running.
- Run commands and move files over the Cube's own SSH, with host keys checked on every connection.
- Tools for LangChain, CrewAI and the OpenAI Agents SDK, so an agent gets a Linux machine to work in.

Also in Node: [`@krovacloud/sdk`](https://www.npmjs.com/package/@krovacloud/sdk), [`@krovacloud/cli`](https://www.npmjs.com/package/@krovacloud/cli) and [`@krovacloud/mcp`](https://www.npmjs.com/package/@krovacloud/mcp). The REST API is documented at [krova.cloud/docs/api](https://krova.cloud/docs/api).

## Install

Python 3.11 or newer. The current release is `v0.1.1`.

```bash
pip install "krova @ git+https://github.com/krovacloud/krova-python@v0.1.1"
```

Or install the wheel attached to the release:

```bash
pip install "https://github.com/krovacloud/krova-python/releases/download/v0.1.1/krova-0.1.1-py3-none-any.whl"
```

Every release lists the SHA256 of its wheel and sdist in `SHA256SUMS`. The agent framework extras are in [Agent framework tools](#agent-framework-tools).

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
        image="ubuntu-24.04",
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

`Krova(api_key=None, space_id=None, base_url=None)` falls back to `KROVA_API_KEY` and `KROVA_SPACE_ID`. `base_url` is optional: it falls back to `KROVA_BASE_URL`, then to `https://krova.cloud`, and the resolved value is `krova.base_url`.

`image` is an id from the images catalog (`GET /api/v1/images`), for example `ubuntu-24.04` or `ubuntu-24.04-docker`. `create` also takes `region`, `user_data` (a cloud-init script), `termination_protection`, `idle_timeout_minutes` and `idempotency_key`.

## Cubes

| Call | What it does |
| --- | --- |
| `krova.cubes.create(...)` | Create a Cube; it starts out `pending`. |
| `krova.cubes.get(id)` | Get one Cube. |
| `krova.cubes.list()` | List the Space's Cubes. |
| `krova.cubes.rename(id, name)` | Rename the Cube and return it. |
| `krova.cubes.resize(id, vcpu=..., ram_gb=..., disk_gb=...)` | Queue a resize of the sizes you pass. Returns the queued job: `job_id`, `is_live`, `requires_restart`, `previous` and `requested`. |
| `krova.cubes.set_idle_timeout(id, minutes)` | Set the idle auto-stop timeout (10 to 10080 minutes), or pass `None` to turn it off. |
| `krova.cubes.ssh(id)` | Read the Cube's SSH host, port, user and host keys. |
| `krova.cubes.connect(id, private_key=...)` | Open an SSH connection to run commands and move files. |
| `krova.cubes.power_off(id)` | Power the Cube off. |
| `krova.cubes.delete(id)` | Delete the Cube. |

A `Cube` has `id`, `name`, `state`, `public_ipv4`, `ssh_user`, `idle_timeout_minutes` and `last_active_at`, and the same actions as methods: `cube.refresh()`, `cube.rename(name)`, `cube.resize(...)`, `cube.set_idle_timeout(minutes)`, `cube.ssh()`, `cube.connect(...)`, `cube.power_off()`, `cube.delete()` and `cube.wait_until_running(timeout=300)`.

Idle auto-stop powers a Cube off after the number of idle minutes you set, and keeps its disk. Set it when you create the Cube (`idle_timeout_minutes=30`) or any time after with `set_idle_timeout`. A resize only changes the sizes you pass; the Cube keeps its current size until the queued job finishes, and disk can only grow.

## Run commands and move files

Commands and files go over the Cube's own SSH, with the private key that matches the `ssh_public_key` you gave the Cube.

```python
with krova.cubes.connect(cube.id, private_key=open("id_ed25519").read()) as shell:
    result = shell.run(["git", "status"], cwd="/srv/app", env={"CI": "1"}, timeout=60)
    print(result.exit_code, result.stdout, result.stderr)

    shell.files.write("/srv/app/.env", "MODE=prod\n")
    data = shell.files.read("/srv/app/.env")
    shell.files.upload("build.tar.gz", "/tmp/build.tar.gz")
    shell.files.download("/var/log/app.log", "app.log")
```

`cube.connect(...)` does the same. `private_key` is an OpenSSH or PEM string (Ed25519, ECDSA or RSA) or a `paramiko.PKey`; add `passphrase=` for an encrypted key. Your SSH agent and `~/.ssh` are not used.

`run` takes a string, which the remote shell runs as written, or a list, where each item is quoted as one argument. `cwd` and `env` values are quoted for you, and env names must match `[A-Za-z_][A-Za-z0-9_]*`. A non-zero exit code comes back in `RunResult.exit_code` and does not raise; `RunTimeoutError` is raised when `timeout` runs out. File paths go to SFTP as written, with no `~` expansion.

The Cube's host keys come from the API and are checked on every connection. If the server presents any other key, or the API has no keys for the Cube yet because it is still booting, `HostKeyMismatchError` is raised and nothing is sent. Pass `host_keys=[...]` to use keys you already hold.

## Agent framework tools

Give an agent three tools bound to one open `CubeShell`: `krova_run(command, cwd=None, timeout=None)`, `krova_read_file(path)` and `krova_write_file(path, content)`. Commands run in the Cube, a Linux VM, over SSH, as the user you connected with, so give each agent a Cube of its own. Each tool returns text. `krova_run` returns the exit code, stdout and stderr, and an error comes back as text starting with `Error:` so the model can react. Stdout, stderr and a file read are each cut at 32 KB, and the result says when they were; pass `max_output_bytes=` to `krova_tools` to change it. You close the shell.

Each framework is an optional extra. `krova[crewai]` and `krova[openai-agents]` need different `openai` majors, so install only one of those two in an environment.

LangChain (`pip install "krova[langchain] @ git+https://github.com/krovacloud/krova-python@v0.1.1"`):

```python
from krova.integrations.langchain import krova_tools

with krova.cubes.connect(cube.id, private_key=key) as shell:
    tools = krova_tools(shell)  # list of BaseTool, for example model.bind_tools(tools)
```

CrewAI (`pip install "krova[crewai] @ git+https://github.com/krovacloud/krova-python@v0.1.1"`):

```python
from crewai import Agent
from krova.integrations.crewai import krova_tools

with krova.cubes.connect(cube.id, private_key=key) as shell:
    coder = Agent(role="Engineer", goal="Fix the build", backstory="...", tools=krova_tools(shell))
```

OpenAI Agents SDK (`pip install "krova[openai-agents] @ git+https://github.com/krovacloud/krova-python@v0.1.1"`):

```python
from agents import Agent, Runner
from krova.integrations.openai_agents import krova_tools

with krova.cubes.connect(cube.id, private_key=key) as shell:
    agent = Agent(name="Engineer", instructions="Fix the build.", tools=krova_tools(shell))
    result = Runner.run_sync(agent, "Run the tests in /srv/app")
```

## Errors

A failed call raises `krova.KrovaError` with `status`, `code`, `message` and `request_id`. Quote the request id when you contact [support](https://krova.cloud/contact). Deleting a Cube with termination protection raises it with status 409 and code `termination_protected`.

`wait_until_running` raises `WaitTimeoutError` on timeout and `CubeFailedError` if the Cube ends up in `error`, `deleted`, `stopped` or `stopping`. Both are `KrovaError` subclasses, as are `HostKeyMismatchError`, `PrivateKeyError` and `RunTimeoutError`.

## Development

```bash
uv sync
uv run ruff check .
uv run pytest
```

The framework adapter tests skip when their framework is not installed. To run one, sync with its extra, for example `uv sync --extra langchain && uv run pytest tests/test_integration_langchain.py`.

The HTTP layer in `krova/_generated/` is generated from `openapi.json` with a pinned `openapi-python-client`. Do not edit it by hand. To refresh it:

```bash
curl -fsSL https://krova.cloud/api/v1/openapi.json -o openapi.json
scripts/generate.sh
```

The hand-written API is `krova/client.py`, `krova/cubes.py`, `krova/shell.py` and `krova/errors.py`.

## Releasing

Bump `version` in `pyproject.toml`, merge, then push a tag that matches it, for example `v0.1.2`. The `Release` workflow builds the wheel and sdist, checks the tag against `pyproject.toml`, and attaches both to a GitHub Release with a `SHA256SUMS` file.

## License

MIT, see [LICENSE](LICENSE).
