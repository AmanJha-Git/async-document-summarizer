# Async Multi-Source Document Summarizer

An asynchronous Python project for extracting structured metadata and summaries
from documents, generating NumPy vectors, and saving the results.

## Setup

Requires Python 3.11 or newer.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Keep API credentials in environment variables; do not commit secrets. The LLM
provider will be selected when the API integration is implemented.

## Current status

Project environment and package scaffolding are in place. Document loading,
LLM integration, vector generation, and output writing are the next stages.