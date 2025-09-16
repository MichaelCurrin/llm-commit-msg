import builtins
import logging
import types
from unittest.mock import Mock, patch

import pytest

from llmcommitmsg.llm import (
    _get_openai_client,
    _request,
    _request_llm,
    generate_commit_msg,
)


class DummyMessage:
    def __init__(self, content: str) -> None:
        self.content = content


class DummyChoice:
    def __init__(self, content: str) -> None:
        self.message = DummyMessage(content)


class DummyResponse:
    def __init__(self, content: str) -> None:
        self.choices = [DummyChoice(content)]


@pytest.fixture()
def mock_openai_client() -> Mock:
    client = Mock()

    client.chat = types.SimpleNamespace(completions=Mock())
    resp = DummyResponse("feat: add tests\n\nAdd pytest test suite.")
    client.chat.completions.create = Mock(return_value=resp)

    return client


def test__request__calls_openai_and_returns_content(mock_openai_client: Mock) -> None:
    result = _request(
        client=mock_openai_client,
        model_name="dummy-model",
        system_prompt="system",
        user_prompt="user",
    )

    assert "feat: add tests" in result
    mock_openai_client.chat.completions.create.assert_called_once()


@patch("llmcommitmsg.llm.OpenAI")
def test__get_openai_client__instantiates_with_api_key_and_host(
    mock_openai_cls: Mock,
) -> None:
    fake_client = object()
    mock_openai_cls.return_value = fake_client

    out = _get_openai_client("abc", "https://host")

    assert out is fake_client
    mock_openai_cls.assert_called_once_with(api_key="abc", base_url="https://host")


def test__request__raises_on_empty_content(mock_openai_client: Mock) -> None:
    mock_openai_client.chat.completions.create.return_value = DummyResponse("")

    with pytest.raises(ValueError):
        _request(mock_openai_client, "m", "s", "u")


def test__request__logs_and_raises_on_api_error(
    mock_openai_client: Mock, caplog: pytest.LogCaptureFixture
) -> None:
    def raise_err(*args, **kwargs):
        raise RuntimeError("boom")

    mock_openai_client.chat.completions.create.side_effect = raise_err

    with caplog.at_level(logging.ERROR), pytest.raises(RuntimeError):
        _request(mock_openai_client, "m", "s", "u")
    assert any("Error in API request" in rec.message for rec in caplog.records)


def test__request_llm__builds_prompt_and_uses_constants(
    mock_openai_client: Mock,
) -> None:
    res = _request_llm(mock_openai_client, "dummy", diff_content="diff here")
    assert "feat: add tests" in res

    _args, kwargs = mock_openai_client.chat.completions.create.call_args

    assert kwargs["model"] == "dummy"
    assert any(m.get("role") == "system" for m in kwargs["messages"])
    assert any("diff here" in m.get("content", "") for m in kwargs["messages"])


@patch("llmcommitmsg.llm._get_openai_client")
def test__generate_commit_msg__uses_client_factory(
    mock_factory: Mock, mock_openai_client: Mock
) -> None:
    mock_factory.return_value = mock_openai_client
    out = generate_commit_msg("some diff")

    assert "feat: add tests" in out
    mock_factory.assert_called_once()
