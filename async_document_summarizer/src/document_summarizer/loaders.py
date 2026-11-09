from pathlib import Path
from pypdf import PdfReader
from document_summarizer.models import Document

class TextFileLoader:
    async def load(self, file_path: str | Path) -> Document:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        
        if path.suffix.lower() == ".pdf":
            return await PDFFileLoader().load(path)
            
        if path.suffix.lower() != ".txt":
            raise ValueError(f"Unsupported file format: {path.suffix}. Only .txt and .pdf files are supported.")

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        return Document(
            source=path,
            title=path.stem,
            text=text
        )

class PDFFileLoader:
    async def load(self, file_path: str | Path) -> Document:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"PDF file not found: {path}")

        reader = PdfReader(path)
        text_content = []
        
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text_content.append(extracted)

        full_text = "\n".join(text_content)
        title = path.stem

        return Document(
            source=path,
            title=title,
            text=full_text
        )