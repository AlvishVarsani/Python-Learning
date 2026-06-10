from openai import OpenAI 

client=OpenAI(
    api_key="YOUR_GROQ_API_KEY",
              base_url="https://api.groq.com/openai/v1")

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in one short sentence."}
    ]
)
print(response.choices.message.content)