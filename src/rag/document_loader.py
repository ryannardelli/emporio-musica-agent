import re
from pypdf import PdfReader


def load_document(path):
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    text = re.sub(r"\s+", " ", text)

    return text


def split_text(text, chunk_size=800, overlap=150):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        if end < len(text):
            end = text.rfind(".", start, end)

            if end == -1 or end <= start:
                end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start = end - overlap

    return chunks