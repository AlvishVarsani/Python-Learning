from openai import OpenAI

from config.config import GROQ_API_KEY, GROQ_BASE_URL, GROQ_MODEL


class GroqService:

    def __init__(
        self,
        api_key: str = GROQ_API_KEY,
        base_url: str = GROQ_BASE_URL,
        model: str = GROQ_MODEL
    ):

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        self.model = model

    def generate(
        self,
        prompt: str
    ) -> str:

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0

        )

        return response.choices[0].message.content