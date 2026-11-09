import os
import sys
import streamlit as st
from pathlib import Path
from pypdf import PdfReader

# Add the src directory to Python's import path
APP_DIR = Path(__file__).resolve().parent
SRC_DIR = APP_DIR / "src"

sys.path.insert(0, str(SRC_DIR))

# Correct import matching your actual folder structure (src -> document_summarizer)
from document_summarizer.summarizer import LLMSummarizer

class Document:
    def __init__(self, source: Path, title: str, text: str):
        self.source = source
        self.title = title
        self.text = text

st.set_page_config(page_title="AI Document Summarizer", page_icon="📄", layout="centered")

st.title("📄 AI Document Summarizer")
st.write("Upload a PDF or text document to get an instant summary powered by Gemini.")

# Secure API Key input for users visiting your site
api_key_input = st.text_input("Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))

uploaded_file = st.file_uploader("Choose a document", type=["txt", "pdf"])

if uploaded_file is not None:
    temp_path = Path("temp_" + uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        if temp_path.suffix.lower() == ".pdf":
            reader = PdfReader(temp_path)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        else:
            text = temp_path.read_text(encoding="utf-8")

        document = Document(source=temp_path, title=uploaded_file.name, text=text)
    finally:
        if temp_path.exists():
            temp_path.unlink()

    if st.button("Generate Summary"):
        if not api_key_input:
            st.error("Please enter a valid Gemini API Key.")
        elif not text.strip():
            st.warning("The uploaded document appears to be empty.")
        else:
            with st.spinner("⏳ Connecting to Gemini..."):
                try:
                    summarizer = LLMSummarizer(api_key=api_key_input)
                    summary = summarizer.summarize(document)
                    
                    st.success("Summary generated successfully!")
                    st.markdown("### 📌 Summary Result")
                    st.write(summary)
                except Exception as e:
                    st.error(f"An error occurred: {e}")