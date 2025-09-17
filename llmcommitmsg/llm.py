"""
LLM module.
"""

import logging

from openai import OpenAI

from .constants import API_HOST, API_KEY, MODEL_NAME, SYSTEM_PROMPT, USER_PROMPT

logger = logging.getLogger(__name__)


def _get_openai_client(api_key: str, api_host: str) -> OpenAI:
    """
    Create and return an OpenAI client instance.
    """
    return OpenAI(api_key=api_key, base_url=api_host)


def _request(
    client: OpenAI, model_name: str, system_prompt: str, user_prompt: str
) -> str:
    """
    Send a request to the OpenAI API and return the response.
    """
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
    except Exception:
        logger.exception("Error in API request")
        raise

    assert response.choices[0], "No results returned"
    message = response.choices[0].message

    if not message.content:
        raise ValueError("No content returned")

    return message.content.strip()


def _request_llm(client: OpenAI, model_name: str, diff_content: str) -> str:
    """
    Generate a commit message using an LLM model and diff content.
    """
    logger.info("Requesting LLM")
    user_prompt = f"{USER_PROMPT}\n\n{diff_content}"

    return _request(client, model_name, SYSTEM_PROMPT, user_prompt)


def generate_commit_msg(diff_content: str) -> str:
    """
    Return a generated commit message.
    """
    client = _get_openai_client(API_KEY, API_HOST)

    return _request_llm(client, MODEL_NAME, diff_content)
