from pathlib import Path
import pytest
from pydantic import ValidationError

from document_summarizer.loaders import TextFileLoader
from document_summarizer.models import Document

@pytest.mark.asyncio  # <--- Add this decorator here
async def test_loader_reads_text_file(tmp_path: Path) -> None:
    source = tmp_path / "article.txt"
    source.write_text("An article about async Python.", encoding="utf-8")

    document = await TextFileLoader().load(source)

    assert document.source == source.resolve()
    assert document.title == "article"
    assert document.text == "An article about async Python."

@pytest.mark.asyncio  # <--- Add this decorator here
async def test_loader_rejects_non_text_file(tmp_path: Path) -> None:
    source = tmp_path / "article.md"
    source.write_text("Markdown content", encoding="utf-8")

    with pytest.raises(ValueError, match="Only \\.txt files are supported"):
        await TextFileLoader().load(source)

@pytest.mark.asyncio  # <--- Add this decorator here
async def test_loader_propagates_missing_file_error(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        await TextFileLoader().load(tmp_path / "missing.txt")

def test_document_rejects_blank_text(tmp_path: Path) -> None:
    # This one is a normal sync function (no async def), so it doesn't need the mark
    with pytest.raises(ValidationError, match="Document text must not be blank"):
        Document(source=tmp_path / "blank.txt", title="blank", text=" \n")