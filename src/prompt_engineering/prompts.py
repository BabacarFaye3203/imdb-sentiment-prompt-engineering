# Zero-shot prompting
def zero_shot_prompt(review: str) -> str:
    return f"""
You are a sentiment analysis assistant.

Analyze the sentiment of the following movie review.

Classify it into exactly one of these categories:
- positive
- negative

IMPORTANT:
Return ONLY the label: positive or negative.
Do not provide explanations.
Do not include any additional text.

Movie review:
{review}

Sentiment:
"""

# Few-shot prompting
def few_shot_prompt(review: str, examples) -> str:

    examples_text = ""

    for _, row in examples.iterrows():
        examples_text += f"""
Movie review:
{row['review']}

Sentiment: {row['sentiment']}
"""

    return f"""
You are a sentiment analysis assistant.

Here are some examples of movie reviews and their sentiments:

{examples_text}

Now analyze the following movie review.

Classify the review into exactly one category:
- positive
- negative

IMPORTANT:
Return ONLY the label: positive or negative.
Do not provide explanations.
Do not include any additional text.

Movie review:
{review}

Sentiment:
"""

def role_based_prompt(review: str) -> str:
    return f"""
You are an expert film critic and sentiment analysis specialist.

You have extensive experience analyzing movie reviews,
identifying opinions, emotions, and subjective expressions.

Your task is to determine the overall sentiment
expressed by the reviewer.

Classify the review into exactly one category:
- positive
- negative

IMPORTANT:
Return ONLY the label: positive or negative.
Do not provide explanations.
Do not include any additional text.

Movie review:
{review}

Sentiment:
"""


def structured_prompt(review: str) -> str:
    return f"""
You are a sentiment analysis assistant.

Analyze the overall sentiment of the following movie review.

You MUST classify the review into exactly one of these two categories:
- positive
- negative

If the review contains both positive and negative opinions,
identify the dominant overall sentiment.

IMPORTANT:
- Never return "mixed", "neutral", or any other category.
- Always choose either "positive" or "negative".
- Return ONLY a valid JSON object.
- The JSON must contain exactly one key: "sentiment".
- Do not include explanations or Markdown.

Expected format:
{{
    "sentiment": "positive"
}}

Movie review:
{review}
"""