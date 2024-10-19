from typing import Optional
from fastapi import HTTPException
from openai import OpenAI
from .models import ResponseModel

class OpenAIService:
    def __init__(self, api_key: str):
        self.openai = OpenAI(api_key=api_key)

    async def generate_text(self, text: str, model: str, temperature: Optional[float] = 0.7, max_tokens: Optional[int] = 2048) -> ResponseModel:
        try:
            response = await self.openai.completions.create(
                model=model,
                prompt=text,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return ResponseModel(text=response.choices[0].text)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating text: {e}")

    async def translate_text(self, text: str, model: str, target_language: str) -> ResponseModel:
        try:
            response = await self.openai.translations.create(
                model=model,
                prompt=text,
                target_language=target_language,
            )
            return ResponseModel(text=response.choices[0].text)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error translating text: {e}")