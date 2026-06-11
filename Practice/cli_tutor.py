from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client=OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_BASE_URL")
)

user_input = input("Ask a question: ")
try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a Java Mentor."},
            {"role": "user", "content": user_input}
    ]
),

except Exception as e:
    print(f"An error occurred: {e}")

first_answer = response.choices[0].message.content
print(first_answer)
input2=input("Do you want a detailed answer? (yes/no): ")
if input2.lower() == "yes":
 input3=input("Please provide more details about your question: ")
 response2=client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": f"You are a helpful assistant. The question is classified as: {first_answer}."},
        {"role": "user", "content": input3},
        {"role":"assistant", "content": "Please provide a detailed answer to the user's question."}
    ]
)
print(response2.choices[0].message.content)