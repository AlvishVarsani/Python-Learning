from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL")  

client = OpenAI(
  api_key=GROQ_API_KEY,
  base_url=GROQ_BASE_URL
)

# List all models and print their IDs
models = client.models.list()
for model in models.data:
    print(model.id)
    
# Retrieve a specific model and print its metadata ,check context window size and other details
model=client.models.retrieve("llama-3.3-70b-versatile")
print(model.model_dump())    