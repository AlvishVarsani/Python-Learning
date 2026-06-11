import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")
GROQ_BASE_URL=os.getenv("GROQ_BASE_URL")
if not GROQ_BASE_URL:
    raise ValueError("GROQ_BASE_URL is not set in the environment variables.")
