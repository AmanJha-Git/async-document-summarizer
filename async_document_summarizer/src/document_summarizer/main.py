import argparse
import asyncio
import sys
from document_summarizer.loaders import TextFileLoader
from document_summarizer.summarizer import LLMSummarizer

async def main():
    parser = argparse.ArgumentParser(description="Load and summarize a text file using Gemini.")
    parser.add_argument("file_path", type=str, help="Path to the .txt file you want to summarize.")
    parser.add_argument("--model", type=str, default="gemini-3.8-flash", help="The Gemini model to use.")
    
    args = parser.parse_args()

    loader = TextFileLoader()
    summarizer = LLMSummarizer(model=args.model)

    print(f"📂 Loading document from: {args.file_path}...")
    try:
        # 1. Load document asynchronously
        document = await loader.load(args.file_path)
        print(f"✅ Loaded successfully! Title: '{document.title}'")

        print(f"🤖 Generating summary using Gemini ({args.model})...")
        # 2. Summarize synchronously (avoids all Windows event loop hanging)
        summary = summarizer.summarize(document)

        print("\n" + "="*30)
        print("📌 SUMMARY RESULT:")
        print("="*30)
        print(summary)
        print("="*30 + "\n")

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())