
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

from prompt_engineering.prompts import structured_prompt
from prompt_engineering.llm_client import (
    generate_response,
    normalize_json_sentiment,
)


app = FastAPI(
    title="IMDB Sentiment Analysis API",
    description="Movie review sentiment classification using Llama 3.2 and Prompt Engineering.",
    version="1.0.0",
)


# Request schema
class SentimentRequest(BaseModel):
    review: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="Movie review to classify",
        examples=["This movie was absolutely fantastic!"]
    )


# Response schema
class SentimentResponse(BaseModel):
    sentiment: Literal["positive", "negative"]
    model: str


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "IMDB Sentiment Analysis API"
    }


@app.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: SentimentRequest):

    try:
        # 1. Build the structured prompt
        prompt = structured_prompt(request.review)

        # 2. Generate response with Ollama
        raw_response = generate_response(prompt)

        # 3. Normalize the JSON sentiment
        sentiment = normalize_json_sentiment(raw_response)

        if sentiment not in {"positive", "negative"}:
            raise HTTPException(
                status_code=502,
                detail="Invalid response received from the LLM."
            )

        return SentimentResponse(
            sentiment=sentiment,
            model="llama3.2"
        )

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=f"LLM service error: {str(error)}"
        )
