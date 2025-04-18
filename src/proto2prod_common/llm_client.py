import os
import openai

class LLMClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.api_key)

    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.completions.create(prompt=prompt, **kwargs)
        return response.choices[0].text
