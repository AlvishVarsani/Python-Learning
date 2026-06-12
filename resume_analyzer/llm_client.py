import openai
from openai import OpenAI
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

from config import GROQ_API_KEY, GROQ_BASE_URL,GROQ_MODEL
from exceptions import RateLimitError, NetworkError, LLMAPIError

# Initialize OpenAI client with Groq's base URL and API key
client = OpenAI(
    api_key=GROQ_API_KEY ,
    base_url=GROQ_BASE_URL,
)

def _is_rate_limit_error(exception):
    if isinstance(exception, openai.RateLimitError):
        return True
    return False

def _is_network_error(exception):
    if isinstance(exception, (openai.APIConnectionError, openai.APITimeoutError)):
        return True
    return False

@retry(
    wait=wait_exponential(multiplier=1, min=2, max=10),
    stop=stop_after_attempt(3),
    retry=retry_if_exception_type((openai.RateLimitError, openai.APIConnectionError, openai.APITimeoutError)),
    reraise=True
)
def stream_llm_response(prompt: str, model: str = GROQ_MODEL, temperature: float = 0.5, top_p: float = 1.0, max_tokens: int = 1024):
    """
    Streams the LLM response with built-in retry logic for rate limits and network errors.
    """

    try:
        stream = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert HR recruiter and technical resume analyzer."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            stream=True
        )

        for chunk in stream:
            if chunk.choices:
                content = chunk.choices[0].delta.content
                
                if content:
                    yield content

    except openai.RateLimitError as e:
        raise RateLimitError(f"Rate limit exceeded: {e}")
    except (openai.APIConnectionError, openai.APITimeoutError) as e:
        raise NetworkError(f"Network error while connecting to LLM API: {e}")
    except openai.APIError as e:
        raise LLMAPIError(f"LLM API Error: {e}")
    except Exception as e:
        raise LLMAPIError(f"An unexpected error occurred: {e}")
