import os
from typing import Optional
from google import genai
from document_summarizer.models import Document

class LLMSummarizer:
    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-3.8-flash"):
        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = os.getenv("GEMINI_API_KEY")
            
        self.model = model

    def summarize(self, document: Document) -> str:
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")

        client = genai.Client(api_key=self.api_key)

        prompt = f"Please summarize the following document titled '{document.title}' concisely:\n\n{document.text}"

        print("⏳ Connecting to Gemini API...")
        
        response = client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        if not response or not response.text:
            raise RuntimeError("Received empty response from Gemini API")

        return response.text.strip()