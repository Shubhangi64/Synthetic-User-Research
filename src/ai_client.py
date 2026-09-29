import json
import time

from google import genai
from google.genai import types

from .config import GEMINI_API_KEY, MODEL


_client = None


def get_client():
    global _client

    if _client is not None:
        return _client

    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Create .env using .env.example."
        )

    _client = genai.Client(
        api_key=GEMINI_API_KEY
    )

    return _client


def generate_text(prompt, retries=2):

    client = get_client()
    last_error = None

    for attempt in range(1, retries + 1):

        try:

            print(
                f"Gemini request attempt "
                f"{attempt}/{retries}..."
            )

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            if not response.text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return response.text.strip()

        except Exception as exc:

            last_error = exc
            error_text = str(exc)

            # Do not repeatedly retry quota/authentication
            # or invalid-request errors.
            permanent_errors = [
                "429",
                "RESOURCE_EXHAUSTED",
                "API_KEY_INVALID",
                "401",
                "403",
                "404",
                "INVALID_ARGUMENT",
            ]

            if any(
                error in error_text
                for error in permanent_errors
            ):
                raise RuntimeError(
                    f"Gemini API error: {error_text}"
                )

            if attempt < retries:

                wait = min(
                    3 * attempt,
                    10
                )

                print(
                    f"Temporary API error. "
                    f"Retrying in {wait}s..."
                )

                time.sleep(wait)

    raise RuntimeError(
        f"Gemini request failed: {last_error}"
    )


def generate_json(prompt, retries=2):

    client = get_client()
    last_error = None

    for attempt in range(1, retries + 1):

        try:

            print(
                f"Gemini JSON request attempt "
                f"{attempt}/{retries}..."
            )

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )

            if not response.text:

                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            result = json.loads(
                response.text
            )

            print("Gemini JSON response received.")

            return result

        except json.JSONDecodeError as exc:

            last_error = exc

            print(
                "Gemini returned invalid JSON."
            )

            if attempt < retries:

                print(
                    "Retrying JSON request in 2s..."
                )

                time.sleep(2)

        except Exception as exc:

            last_error = exc
            error_text = str(exc)

            permanent_errors = [
                "429",
                "RESOURCE_EXHAUSTED",
                "API_KEY_INVALID",
                "401",
                "403",
                "404",
                "INVALID_ARGUMENT",
            ]

            # These errors normally will not be fixed
            # by sending the same request again.
            if any(
                error in error_text
                for error in permanent_errors
            ):

                raise RuntimeError(
                    f"Gemini API error: {error_text}"
                )

            if attempt < retries:

                wait = min(
                    3 * attempt,
                    10
                )

                print(
                    f"Temporary API error. "
                    f"Retrying in {wait}s..."
                )

                time.sleep(wait)

    raise RuntimeError(
        f"Gemini JSON request failed: {last_error}"
    )


def test_connection():

    text = generate_text(
        "Reply with exactly: "
        "Gemini connection successful."
    )

    return "successful" in text.lower()
