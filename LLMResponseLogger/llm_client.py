import requests

class LLMClient:
    def __init__(self, api_key, base_url, model,timeout):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.timeout = timeout

    def generate(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }
        
        response = requests.post(f"{self.base_url}/chat/completions", json=payload, headers=headers,timeout=self.timeout)
        data=response.json()
        if not data.get("choices"):
            raise ValueError("No choices returned from API.")
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]