import os
import requests
from dotenv import load_dotenv

load_dotenv()

COHERE_KEY = os.getenv("COHERE_API_KEY")
API_URL = "https://api.cohere.com/v1/embed"

def get_embedding(text):
    headers = {
        "Authorization": f"Bearer {COHERE_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "texts": [text],
        "model": "embed-english-v3.0",
        "input_type": "search_document"
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()["embeddings"][0]
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None

print(get_embedding("Forget my password"))