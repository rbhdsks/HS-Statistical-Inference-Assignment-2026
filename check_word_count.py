from pathlib import Path
import re
import pymupdf

PDF_PATH = Path("Statistical_Inference_Assignment.pdf")

if not PDF_PATH.is_file():
    raise FileNotFoundError(f"PDF not found: {PDF_PATH.resolve()}")

total_words = 0

with pymupdf.open(PDF_PATH) as document:
    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text", sort=True)

        # Join words broken across lines, e.g. "develop-\nment".
        text = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", text)

        # Count words and numbers; retain internal hyphens/apostrophes.
        words = re.findall(r"\b\w+(?:[-’']\w+)*\b", text)
        count = len(words)
        total_words += count

        print(f"Page {page_number:2}: {count:4} words")

    print(f"\nTotal pages: {len(document)}")
    print(f"Total extracted words: {total_words:,}")