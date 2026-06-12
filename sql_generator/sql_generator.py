import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


api_key = os.getenv("GROQ_API_KEY")  # Using the same key name as in the resume analyzer for consistency

if not api_key:
    raise ValueError("Missing GROQ_API_KEY. Please set it in your .env file or environment variables.")

client = OpenAI(
    api_key=api_key,
    base_url=os.getenv("GROQ_BASE_URL")
)

def generate_sql(prompt_text, temperature):
    print("\n" + "-" * 50)
    print(f"Temperature: {temperature}")
    print("-" * 50)

    try:
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL"),
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert SQL developer. Return ONLY SQL queries."
                },
                {
                    "role": "user",
                    "content": prompt_text
                }
            ],
            temperature=temperature,
        )

        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error generating SQL: {e}")

if __name__ == "__main__":

    prompt = (
        "Create a table for an online store to store customer orders, "
        "and write a query to find top 5 customers by total spending."
    )

    generate_sql(prompt, 0.0)
    generate_sql(prompt, 0.5)
    generate_sql(prompt, 1.0)