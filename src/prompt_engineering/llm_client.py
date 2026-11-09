
import json
import os
import re

from langchain_ollama import ChatOllama


# Ollama configuration
OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2"
)


# Initialize the local LLM
llm = ChatOllama(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=0
)


def generate_response(prompt: str) -> str:
    """
    Generate a response using the configured Ollama model.
    """
    response = llm.invoke(prompt)
    return response.content


def normalize_sentiment(response: str) -> str:
    text = response.strip().lower()

    if text in {"positive", "negative"}:
        return text

    match = re.search(
        r"^\s*\*{0,2}(positive|negative)\*{0,2}\s*[.!]?\s*$",
        text
    )

    if match:
        return match.group(1)

    return "unknown"


def normalize_json_sentiment(response: str) -> str:
    try:
        data = json.loads(response)

        sentiment = data.get("sentiment", "").strip().lower()

        if sentiment in {"positive", "negative"}:
            return sentiment

        return "unknown"

    except (json.JSONDecodeError, AttributeError):
        return "unknown"
