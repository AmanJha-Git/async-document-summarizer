
import sys
import streamlit as st
from pathlib import Path
from pypdf import PdfReader

# Add the src directory to Python's import path
APP_DIR = Path(__file__).resolve().parent
SRC_DIR = APP_DIR / "src"

sys.path.insert(0, str(SRC_DIR))

# Import the summarizer
from document_summarizer.summarizer import LLMSummarizer


# Document class
class Document:
    def __init__(self, source: Path, title: str, text: str):
        self.source = source
        self.title = title
        self.text = text


# Streamlit page configuration
st.set_page_config(
    page_title="AI Document Summarizer",
    page_icon="📄",
    layout="centered"
)

# Application title
st.title("📄 AI Document Summarizer")

st.write(
    "Upload a PDF or text document to get an instant summary powered by Gemini."
)


# Retrieve Gemini API key from Streamlit Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error(
        "Gemini API key is not configured. "
        "Please add GEMINI_API_KEY in Streamlit Cloud Secrets."
    )
    st.stop()


# Document uploader
uploaded_file = st.file_uploader(
    "Choose a document",
    type=["txt", "pdf"]
)


if uploaded_file is not None:

    # Read uploaded document
    try:
        if uploaded_file.name.lower().endswith(".pdf"):

            reader = PdfReader(uploaded_file)

            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        else:
            text = uploaded_file.getvalue().decode("utf-8")

        document = Document(
            source=Path(uploaded_file.name),
            title=uploaded_file.name,
            text=text
        )

        st.success(f"Uploaded successfully: {uploaded_file.name}")

    except Exception as e:
        st.error(f"Error reading document: {e}")
        st.stop()


    # Generate summary button
    if st.button("Generate Summary", type="primary"):

        if not text.strip():

            st.warning(
                "The uploaded document appears to be empty "
                "or contains no extractable text."
            )

        else:

            with st.spinner("⏳ Connecting to Gemini..."):

                try:
                    summarizer = LLMSummarizer(api_key=api_key)

                    summary = summarizer.summarize(document)

                    st.success("Summary generated successfully!")

                    st.markdown("### 📌 Summary Result")

                    st.write(summary)

                except Exception as e:

                    st.error(f"An error occurred: {e}")
