from pathlib import Path

from pydantic import BaseModel, field_validator


class Document(BaseModel):
    source: Path
    title: str
    text: str

    @field_validator("text")
    @classmethod
    def text_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Document text must not be blank")
        return value