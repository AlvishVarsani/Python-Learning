import time
import logging
from openai import OpenAI
from config import GROQ_API_KEY, GROQ_BASE_URL

logging.basicConfig(level=logging.INFO)

class ChatService:
  def __init__(self):
    self.logger = logging.getLogger(self.__class__.__name__)
    self.summary = ""
    self.messages=[{
      "role": "system",
      "content":"""  
      You are a Senior Java Mentor.

      Rules:
      - Explain concepts clearly.
      - Give examples.
      - Answer like a teacher.
      """
    }]

  def ask_question(self,user_input): 
    self.messages.append({
      "role": "user",
      "content": user_input
    }) 

    client=OpenAI(
      api_key=GROQ_API_KEY,
      base_url=GROQ_BASE_URL
    )

    MAX_RETRIES = 3
    for attempt in range(MAX_RETRIES):
      try:
        response = client.chat.completions.create(
          model="openai/gpt-oss-20b",
          messages=self.messages,
          temperature=0.2,
          max_tokens=250,
          timeout=10
        )
        assistant = response.choices[0].message.content
        self.logger.info(f"Assistant response: {assistant} with request ID: {response.id} and response time: {response.response_ms}ms")
        self.messages.append({
          "role": "assistant",
          "content": assistant
        })
        return assistant

      except Exception as e:
        self.logger.error(f"An error occurred: {e}")
        if attempt < MAX_RETRIES - 1:
          wait_time = 2 ** attempt
          self.logger.info(f"Retrying in {wait_time} seconds...")
          time.sleep(wait_time)
        else:
          self.logger.info("Max retries reached. Please try again later.")
        return "Sorry, I'm having trouble processing your request right now. Please try again later."