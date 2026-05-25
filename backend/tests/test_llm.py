from types import SimpleNamespace

import pytest

from app.services import llm


def settings(provider: str, api_key: str | None = None):
    return SimpleNamespace(
        app_env="development",
        demo_mode=False,
        model_provider=provider,
        ai_provider=provider,
        ollama_base_url="http://localhost:11434",
        ollama_chat_model="llama3.2:3b",
        ollama_embedding_model="bge-m3",
        ollama_embed_model="bge-m3",
        embedding_dimension=1024,
        openai_api_key=api_key,
        openai_base_url="https://api.openai.com/v1",
        openai_chat_model="gpt-4o-mini",
        openai_embed_model="text-embedding-3-small",
    )


def test_get_llm_provider_supports_openai(monkeypatch):
    monkeypatch.setattr(llm, "get_settings", lambda: settings("openai", "test-key"))

    provider = llm.get_llm_provider()

    assert isinstance(provider, llm.OpenAIProvider)


def test_openai_provider_requires_api_key(monkeypatch):
    monkeypatch.setattr(llm, "get_settings", lambda: settings("openai"))

    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        llm.get_llm_provider()
