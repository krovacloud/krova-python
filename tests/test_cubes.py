from __future__ import annotations

import json
from types import SimpleNamespace

import httpx
import pytest

import krova.cubes as cubes_module
from krova import CubeFailedError, Krova, KrovaError, WaitTimeoutError

BASE = "https://krova.cloud/api/v1/spaces/spc_1/cubes"


def cube_json(state: str = "pending", cube_id: str = "cub_1") -> dict:
    return {
        "id": cube_id,
        "name": "agent-box",
        "state": state,
        "publicIpv4": "203.0.113.7" if state == "running" else None,
        "resources": {"vcpu": 2, "ramGb": 4, "diskGb": 40},
        "image": "ubuntu-24.04",
        "sshUser": "ubuntu",
        "costPerHour": 0.05,
        "terminationProtection": False,
        "terminationProtectionChangedAt": None,
        "terminationProtectionChangedBy": None,
        "idleTimeoutMinutes": None,
        "lastActiveAt": None,
        "createdAt": "2026-11-16T10:00:00.000Z",
        "updatedAt": "2026-11-16T10:00:00.000Z",
    }


class Recorder:
    """A mock transport that answers from a queue and keeps every request it saw."""

    def __init__(self, *responses: httpx.Response) -> None:
        self.responses = list(responses)
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self.responses.pop(0)


def make_client(*responses: httpx.Response) -> tuple[Krova, Recorder]:
    recorder = Recorder(*responses)
    client = Krova(
        api_key="kro_test",
        space_id="spc_1",
        transport=httpx.MockTransport(recorder),
    )
    return client, recorder


def json_response(status: int, body: object, headers: dict[str, str] | None = None):
    return httpx.Response(status, json=body, headers=headers)


def test_create_sends_the_documented_body_and_auth_header():
    client, rec = make_client(json_response(201, {"cube": cube_json()}))

    cube = client.cubes.create(
        name="agent-box",
        image="ubuntu-24.04",
        vcpu=2,
        ram_gb=4,
        disk_gb=40,
        ssh_public_key="ssh-ed25519 AAAA test",
        region="us-east",
        idempotency_key="once",
    )

    request = rec.requests[0]
    assert request.method == "POST"
    assert str(request.url) == BASE
    assert request.headers["x-api-key"] == "kro_test"
    assert "authorization" not in request.headers
    assert request.headers["idempotency-key"] == "once"
    assert json.loads(request.content) == {
        "name": "agent-box",
        "image": "ubuntu-24.04",
        "resources": {"vcpu": 2, "ramGb": 4, "diskGb": 40},
        "sshPublicKey": "ssh-ed25519 AAAA test",
        "region": "us-east",
        "terminationProtection": False,
    }
    assert cube.id == "cub_1"
    assert cube.state == "pending"
    assert cube.public_ipv4 is None
    assert cube.ssh_user == "ubuntu"


def test_get_returns_a_cube_handle():
    client, rec = make_client(json_response(200, {"cube": cube_json("running")}))

    cube = client.cubes.get("cub_1")

    assert str(rec.requests[0].url) == f"{BASE}/cub_1"
    assert cube.state == "running"
    assert cube.public_ipv4 == "203.0.113.7"


def test_list_returns_every_cube():
    page = {"page": 1, "limit": 50, "total": 2, "totalPages": 1}
    body = {"cubes": [cube_json(cube_id="a"), cube_json(cube_id="b")], "pagination": page}
    client, _ = make_client(json_response(200, body))

    assert [c.id for c in client.cubes.list()] == ["a", "b"]


def test_create_sends_idle_timeout_only_when_given():
    client, rec = make_client(
        json_response(201, {"cube": cube_json()}),
        json_response(201, {"cube": {**cube_json(), "idleTimeoutMinutes": 30}}),
    )
    args = dict(name="a", image="ubuntu-24.04", vcpu=1, ram_gb=1, disk_gb=10, ssh_public_key="k")

    client.cubes.create(**args)
    cube = client.cubes.create(**args, idle_timeout_minutes=30)

    assert "idleTimeoutMinutes" not in json.loads(rec.requests[0].content)
    assert json.loads(rec.requests[1].content)["idleTimeoutMinutes"] == 30
    assert cube.idle_timeout_minutes == 30


def test_cube_exposes_idle_timeout_and_last_active_at():
    body = {
        **cube_json("running"),
        "idleTimeoutMinutes": 45,
        "lastActiveAt": "2026-11-17T08:30:00.000Z",
    }
    client, _ = make_client(json_response(200, {"cube": body}))

    cube = client.cubes.get("cub_1")

    assert cube.idle_timeout_minutes == 45
    assert cube.last_active_at is not None
    assert (cube.last_active_at.year, cube.last_active_at.hour, cube.last_active_at.minute) == (
        2026,
        8,
        30,
    )


def test_cube_defaults_to_no_idle_timeout_and_no_activity():
    client, _ = make_client(json_response(200, {"cube": cube_json("running")}))

    cube = client.cubes.get("cub_1")

    assert cube.idle_timeout_minutes is None
    assert cube.last_active_at is None


def test_rename_patches_only_the_name_and_returns_the_updated_cube():
    client, rec = make_client(json_response(200, {"cube": {**cube_json(), "name": "renamed"}}))

    cube = client.cubes.rename("cub_1", "renamed")

    request = rec.requests[0]
    assert (request.method, request.url.path) == ("PATCH", "/api/v1/spaces/spc_1/cubes/cub_1")
    assert json.loads(request.content) == {"name": "renamed"}
    assert cube.name == "renamed"


def test_cube_handle_rename_updates_the_handle_in_place():
    client, rec = make_client(
        json_response(200, {"cube": cube_json()}),
        json_response(200, {"cube": {**cube_json(), "name": "renamed"}}),
    )
    cube = client.cubes.get("cub_1")

    assert cube.rename("renamed") is cube

    assert cube.name == "renamed"
    assert json.loads(rec.requests[1].content) == {"name": "renamed"}


def test_set_idle_timeout_sends_the_minutes():
    body = {**cube_json("running"), "idleTimeoutMinutes": 60}
    client, rec = make_client(json_response(200, {"cube": body}))

    cube = client.cubes.set_idle_timeout("cub_1", 60)

    request = rec.requests[0]
    assert (request.method, request.url.path) == ("PATCH", "/api/v1/spaces/spc_1/cubes/cub_1")
    assert json.loads(request.content) == {"idleTimeoutMinutes": 60}
    assert cube.idle_timeout_minutes == 60


def test_set_idle_timeout_none_sends_null_to_turn_it_off():
    client, rec = make_client(json_response(200, {"cube": cube_json("running")}))

    cube = client.cubes.set_idle_timeout("cub_1", None)

    assert json.loads(rec.requests[0].content) == {"idleTimeoutMinutes": None}
    assert cube.idle_timeout_minutes is None


def test_cube_handle_set_idle_timeout_updates_the_handle_in_place():
    client, _ = make_client(
        json_response(200, {"cube": cube_json("running")}),
        json_response(200, {"cube": {**cube_json("running"), "idleTimeoutMinutes": 15}}),
    )
    cube = client.cubes.get("cub_1")

    assert cube.set_idle_timeout(15) is cube

    assert cube.idle_timeout_minutes == 15


def test_a_rejected_idle_timeout_raises_the_api_error():
    client, _ = make_client(json_response(400, {"error": "idleTimeoutMinutes must be 10 to 10080"}))

    with pytest.raises(KrovaError) as caught:
        client.cubes.set_idle_timeout("cub_1", 5)

    assert caught.value.status == 400


RESIZE_RESPONSE = {
    "success": True,
    "state": "queued",
    "jobId": "job_7",
    "isLive": False,
    "requiresRestart": True,
    "previous": {"vcpu": 2, "ramGb": 4, "diskGb": 40},
    "requested": {"vcpu": 4, "ramGb": 4, "diskGb": 80},
}


def test_resize_sends_only_the_given_sizes_and_returns_the_queued_job():
    client, rec = make_client(json_response(200, RESIZE_RESPONSE))

    result = client.cubes.resize("cub_1", vcpu=4, disk_gb=80, idempotency_key="resize-once")

    request = rec.requests[0]
    assert (request.method, request.url.path) == (
        "POST",
        "/api/v1/spaces/spc_1/cubes/cub_1/resize",
    )
    assert request.headers["idempotency-key"] == "resize-once"
    assert json.loads(request.content) == {"resources": {"vcpu": 4, "diskGb": 80}}
    assert result.job_id == "job_7"
    assert (result.is_live, result.requires_restart) == (False, True)
    assert (result.previous.vcpu, result.previous.ram_gb, result.previous.disk_gb) == (2, 4, 40)
    assert (result.requested.vcpu, result.requested.ram_gb, result.requested.disk_gb) == (4, 4, 80)


def test_resize_sends_ram_in_gb_and_no_idempotency_header_by_default():
    client, rec = make_client(json_response(200, RESIZE_RESPONSE))

    client.cubes.resize("cub_1", ram_gb=8.5)

    request = rec.requests[0]
    assert json.loads(request.content) == {"resources": {"ramGb": 8.5}}
    assert "idempotency-key" not in request.headers


def test_cube_handle_resize_uses_the_cube_id():
    client, rec = make_client(
        json_response(200, {"cube": cube_json("running")}),
        json_response(200, RESIZE_RESPONSE),
    )
    cube = client.cubes.get("cub_1")

    result = cube.resize(vcpu=4)

    assert rec.requests[1].url.path.endswith("/cubes/cub_1/resize")
    assert result.job_id == "job_7"


def test_resize_conflict_raises_the_api_error():
    client, _ = make_client(json_response(409, {"error": "A resize is already queued"}))

    with pytest.raises(KrovaError) as caught:
        client.cubes.resize("cub_1", vcpu=4)

    assert caught.value.status == 409


def test_delete_and_power_off_hit_the_right_routes():
    client, rec = make_client(
        json_response(200, {"success": True}),
        json_response(200, {"success": True}),
    )

    client.cubes.delete("cub_1")
    client.cubes.power_off("cub_1")

    assert [(r.method, r.url.path) for r in rec.requests] == [
        ("DELETE", "/api/v1/spaces/spc_1/cubes/cub_1"),
        ("POST", "/api/v1/spaces/spc_1/cubes/cub_1/power-off"),
    ]


def test_ssh_returns_host_port_user_and_host_keys():
    body = {
        "host": "cub-1.krova.cloud",
        "port": 22,
        "user": "ubuntu",
        "hostKeys": [{"type": "ssh-ed25519", "key": "AAAAC3"}],
    }
    client, rec = make_client(json_response(200, body))

    info = client.cubes.ssh("cub_1")

    assert rec.requests[0].url.path.endswith("/cubes/cub_1/ssh")
    assert (info.host, info.port, info.user) == ("cub-1.krova.cloud", 22, "ubuntu")
    assert [(k.type, k.key) for k in info.host_keys] == [("ssh-ed25519", "AAAAC3")]


def test_error_carries_status_message_and_request_id():
    client, _ = make_client(
        json_response(404, {"error": "Cube not found"}, {"x-request-id": "req_9"})
    )

    with pytest.raises(KrovaError) as caught:
        client.cubes.get("nope")

    assert caught.value.status == 404
    assert caught.value.message == "Cube not found"
    assert caught.value.request_id == "req_9"
    assert caught.value.code is None
    assert "req_9" in str(caught.value)


def test_termination_protected_delete_exposes_the_code():
    body = {"error": {"code": "termination_protected", "message": "Turn protection off first"}}
    client, _ = make_client(json_response(409, body))

    with pytest.raises(KrovaError) as caught:
        client.cubes.delete("cub_1")

    assert caught.value.status == 409
    assert caught.value.code == "termination_protected"
    assert caught.value.message == "Turn protection off first"


def test_error_code_header_wins_and_a_non_json_body_still_raises():
    client, _ = make_client(
        httpx.Response(502, text="<html>bad gateway</html>", headers={"x-error-code": "upstream"})
    )

    with pytest.raises(KrovaError) as caught:
        client.cubes.list()

    assert caught.value.status == 502
    assert caught.value.code == "upstream"
    assert caught.value.message == "Bad Gateway"


@pytest.fixture
def fake_clock(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Replace time.sleep and time.monotonic in the cubes module; return the sleeps taken."""
    now = [0.0]
    sleeps: list[float] = []

    def sleep(seconds: float) -> None:
        sleeps.append(seconds)
        now[0] += seconds

    monkeypatch.setattr(
        cubes_module, "time", SimpleNamespace(monotonic=lambda: now[0], sleep=sleep)
    )
    return sleeps


def test_wait_until_running_polls_with_growing_bounded_backoff(fake_clock: list[float]):
    states = ["pending", "booting", "booting", "booting", "booting", "running"]
    client, rec = make_client(
        json_response(201, {"cube": cube_json("pending")}),
        *[json_response(200, {"cube": cube_json(s)}) for s in states],
    )
    cube = client.cubes.create(
        name="x", image="i", vcpu=1, ram_gb=1, disk_gb=10, ssh_public_key="ssh-ed25519 A"
    )

    result = cube.wait_until_running(timeout=60, poll_interval=1, max_interval=3)

    assert result is cube
    assert cube.state == "running"
    assert cube.public_ipv4 == "203.0.113.7"
    assert len(rec.requests) == 1 + len(states)
    assert fake_clock == [1, 1.5, 2.25, 3, 3]


def test_wait_until_running_times_out(fake_clock: list[float]):
    client, _ = make_client(
        json_response(201, {"cube": cube_json("pending")}),
        *[json_response(200, {"cube": cube_json("booting")}) for _ in range(20)],
    )
    cube = client.cubes.create(
        name="x", image="i", vcpu=1, ram_gb=1, disk_gb=10, ssh_public_key="ssh-ed25519 A"
    )

    with pytest.raises(WaitTimeoutError) as caught:
        cube.wait_until_running(timeout=5, poll_interval=2, max_interval=2)

    assert caught.value.state == "booting"
    assert caught.value.cube_id == "cub_1"
    assert sum(fake_clock) == pytest.approx(5)


def test_wait_until_running_fails_fast_on_a_dead_state(fake_clock: list[float]):
    client, rec = make_client(json_response(200, {"cube": cube_json("error")}))
    cube = cubes_module.Cube(client.cubes, _data("pending"))

    with pytest.raises(CubeFailedError) as caught:
        cube.wait_until_running(timeout=60)

    assert caught.value.state == "error"
    assert fake_clock == []
    assert len(rec.requests) == 1


def _data(state: str):
    from krova._generated.models.cube import Cube as CubeData

    return CubeData.from_dict(cube_json(state))


def test_wait_until_running_propagates_api_errors(fake_clock: list[float]):
    client, _ = make_client(json_response(404, {"error": "gone"}))
    cube = cubes_module.Cube(client.cubes, _data("pending"))

    with pytest.raises(KrovaError) as caught:
        cube.wait_until_running(timeout=60)

    assert caught.value.status == 404


def test_config_comes_from_the_environment(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("KROVA_API_KEY", "kro_env")
    monkeypatch.setenv("KROVA_SPACE_ID", "spc_env")
    rec = Recorder(json_response(200, {"cube": cube_json()}))

    client = Krova(transport=httpx.MockTransport(rec))
    client.cubes.get("cub_1")

    assert client.space_id == "spc_env"
    assert rec.requests[0].headers["x-api-key"] == "kro_env"
    assert rec.requests[0].url.path == "/api/v1/spaces/spc_env/cubes/cub_1"


def test_missing_key_or_space_is_a_clear_error(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("KROVA_API_KEY", raising=False)
    monkeypatch.delenv("KROVA_SPACE_ID", raising=False)

    with pytest.raises(ValueError, match="KROVA_API_KEY"):
        Krova(space_id="spc_1")
    with pytest.raises(ValueError, match="KROVA_SPACE_ID"):
        Krova(api_key="kro_test")


def test_base_url_may_already_include_the_api_path():
    rec = Recorder(json_response(200, {"cube": cube_json()}))
    client = Krova(
        api_key="k",
        space_id="spc_1",
        base_url="https://staging.example.test/api/v1/",
        transport=httpx.MockTransport(rec),
    )

    client.cubes.get("cub_1")

    assert (
        str(rec.requests[0].url) == "https://staging.example.test/api/v1/spaces/spc_1/cubes/cub_1"
    )


def request_url(client_kwargs: dict) -> tuple[Krova, str]:
    rec = Recorder(json_response(200, {"cube": cube_json()}))
    client = Krova(
        api_key="k", space_id="spc_1", transport=httpx.MockTransport(rec), **client_kwargs
    )
    client.cubes.get("cub_1")
    return client, str(rec.requests[0].url)


def test_base_url_argument_wins_over_the_environment(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("KROVA_BASE_URL", "https://env.example.test")

    client, url = request_url({"base_url": "https://arg.example.test"})

    assert client.base_url == "https://arg.example.test"
    assert url == "https://arg.example.test/api/v1/spaces/spc_1/cubes/cub_1"


def test_base_url_comes_from_the_environment_when_no_argument(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("KROVA_BASE_URL", "https://env.example.test")

    client, url = request_url({})

    assert client.base_url == "https://env.example.test"
    assert url == "https://env.example.test/api/v1/spaces/spc_1/cubes/cub_1"


@pytest.mark.parametrize("blank", ["", "   "])
def test_blank_base_url_counts_as_unset(monkeypatch: pytest.MonkeyPatch, blank: str):
    monkeypatch.setenv("KROVA_BASE_URL", blank)

    client, url = request_url({})
    assert client.base_url == "https://krova.cloud"
    assert url == BASE + "/cub_1"

    monkeypatch.setenv("KROVA_BASE_URL", "https://env.example.test")
    client, _ = request_url({"base_url": blank})
    assert client.base_url == "https://env.example.test"


def test_base_url_defaults_when_neither_argument_nor_environment_is_set():
    client, url = request_url({})

    assert client.base_url == "https://krova.cloud"
    assert url == BASE + "/cub_1"


@pytest.mark.parametrize(
    "given",
    [
        "https://self.example.test",
        "https://self.example.test/",
        "https://self.example.test/api/v1",
        "https://self.example.test/api/v1/",
    ],
)
def test_origin_and_full_api_url_both_resolve_to_the_api_path(
    monkeypatch: pytest.MonkeyPatch, given: str
):
    _, from_argument = request_url({"base_url": given})
    monkeypatch.setenv("KROVA_BASE_URL", given)
    _, from_environment = request_url({})

    expected = "https://self.example.test/api/v1/spaces/spc_1/cubes/cub_1"
    assert from_argument == expected
    assert from_environment == expected
