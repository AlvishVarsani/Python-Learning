import logging
import requests

from config import (
    API_KEY,
    BASE_URL,
    MODEL,
    LOG_FILE,
    REQUEST_TIMEOUT,
)
from llm_client import LLMClient
from logger_service import save_interaction


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def main() :

    if not API_KEY:
        raise ValueError(
            "GROQ_API_KEY environment variable not found."
        )

    client = LLMClient(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=MODEL,
        timeout=REQUEST_TIMEOUT,
    )

    query = input("Enter your prompt: ").strip()

    if not query:
        logger.warning("Prompt cannot be empty.")
        return

    try:
        logger.info("Sending request to LLM.")

        answer = client.generate(query)

        print("\n=== RESPONSE ===\n")
        print(answer)

        save_interaction(
            file_path=LOG_FILE,
            query=query,
            response=answer,
        )

        logger.info(
            "Interaction saved to %s",
            LOG_FILE,
        )

    except requests.exceptions.Timeout:
        logger.exception("Request timed out.")

    except requests.exceptions.RequestException as exc:
        logger.exception(
            "API request failed: %s",
            exc,
        )

    except Exception as exc:
        logger.exception(
            "Unexpected error: %s",
            exc,
        )


if __name__ == "__main__":
    main()