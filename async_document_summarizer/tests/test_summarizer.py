from pathlib import Path
import pytest
from document_summarizer.models import Document
from document_summarizer.summarizer import LLMSummarizer

class MockResponse:
    def __init__(self, text):
        self.text = text

@pytest.mark.asyncio
async def test_llm_summarizer_success(monkeypatch):
    # 1. Mock the async generate_content method on AsyncModels
    async def mock_generate_content(self, *, model, contents, config=None):
        return MockResponse("This is a concise test summary.")

    monkeypatch.setattr("google.genai.models.AsyncModels.generate_content", mock_generate_content)

    # 2. Create a dummy document to summarize
    doc = Document(
        source=Path("test.txt"),
        title="Test Document",
        text="This is a long article about async programming in Python."
    )

    # 3. Initialize the summarizer with a fake API key
    summarizer = LLMSummarizer(api_key="fake-gemini-key")

    # 4. Run the summarizer
    summary = await summarizer.summarize(doc)

    # 5. Assert that we got the expected summary back
    assert summary == "This is a concise test summary."

@pytest.mark.asyncio
async def test_llm_summarizer_raises_error_without_api_key():
    doc = Document(
        source=Path("test.txt"),
        title="Test Document",
        text="Some text here."
    )

    summarizer = LLMSummarizer(api_key="")

    with pytest.raises(ValueError, match="GEMINI_API_KEY environment variable is required"):
        await summarizer.summarize(doc)