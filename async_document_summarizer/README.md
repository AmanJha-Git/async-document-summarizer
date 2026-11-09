# 📄 Async Document Summarizer

An AI-powered document summarization application that uses Google's Gemini API to generate concise summaries from PDF and TXT documents.

Users can upload a document and receive an AI-generated summary through a simple and interactive Streamlit interface.

## 🚀 Live Demo

**[Try AI Document Summarizer](https://async-document-summarizer.streamlit.app/)**

## ✨ Features

- **PDF Support:** Extract and summarize text from PDF documents.
- **TXT Support:** Upload and summarize plain text files.
- **AI-Powered Summarization:** Uses Google's Gemini API to generate meaningful summaries.
- **Interactive Interface:** Simple and user-friendly interface built with Streamlit.
- **Secure API Configuration:** Uses Streamlit Secrets to manage Gemini API credentials.
- **Cloud Deployment:** Hosted on Streamlit Community Cloud.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Google Gemini API | AI-powered summarization |
| google-genai | Gemini API integration |
| PyPDF | PDF text extraction |

## 📂 Project Structure

```text
async-document-summarizer/
│
├── src/
│   └── document_summarizer/
│       ├── __init__.py
│       ├── loaders.py
│       ├── main.py
│       ├── models.py
│       └── summarizer.py
│
├── tests/
│
├── app.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AmanJha-Git/async-document-summarizer.git
```

### 2. Navigate to the project directory

```bash
cd async-document-summarizer/async_document_summarizer
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API Key

Get your Gemini API key from:

https://aistudio.google.com/apikey

For local development, create the following file:

```text
.streamlit/secrets.toml
```

Add your API key:

```toml
GEMINI_API_KEY = "your_actual_gemini_api_key"
```

**Important:** Never commit your API key or `secrets.toml` file to GitHub.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💻 Usage

1. Open the application.
2. Upload a PDF or TXT document.
3. Click **Generate Summary**.
4. Wait for Gemini to process the document.
5. View the generated summary.

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud** and connected to GitHub.

Deployment steps:

1. Push the project to GitHub.
2. Visit https://share.streamlit.io/
3. Connect your GitHub repository.
4. Select `async_document_summarizer/app.py` as the application entry point.
5. Configure `GEMINI_API_KEY` under Streamlit Cloud Secrets.
6. Deploy the application.

## ⚠️ Current Limitations

- Scanned PDFs and image-based documents are not currently supported through OCR.
- PDF summarization depends on successful text extraction.
- Summarization quality depends on the Gemini model and the document content.
- Very large documents may require text chunking to avoid API token limits.

## 🔮 Future Improvements

- [ ] OCR support for scanned PDFs.
- [ ] Multimodal document understanding for images, charts and diagrams.
- [ ] Support for Word documents (DOCX).
- [ ] Chunk-based summarization for large documents.
- [ ] Download summaries as PDF or TXT.
- [ ] Summary length customization.
- [ ] Asynchronous processing for improved responsiveness.

## 👨‍💻 Author

**Aman Jha**

GitHub: https://github.com/AmanJha-Git

---

⭐ If you find this project useful, consider giving the repository a star!