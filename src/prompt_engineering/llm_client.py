import re

from langchain_ollama import ChatOllama

# Initialize the local LLM
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def generate_response(prompt: str) -> str:
    """
    Generate a response using the local Ollama model.
    """
    response = llm.invoke(prompt)
    return response.content

def normalize_sentiment(response: str) -> str:
    text = response.strip().lower()

    # Exact label
    if text in {"positive", "negative"}:
        return text

    # Search for a label at the beginning of the response
    match = re.search(
        r"^\s*\**(positive|negative)\**\s*[.!]?\s*$",
        text
    )

    if match:
        return match.group(1)

    return "unknown"

import json

def normalize_json_sentiment(response: str) -> str:
    try:
        data = json.loads(response)

        sentiment = data.get("sentiment", "").strip().lower()

        if sentiment in {"positive", "negative"}:
            return sentiment

        return "unknown"

    except (json.JSONDecodeError, AttributeError):
        return "unknown"