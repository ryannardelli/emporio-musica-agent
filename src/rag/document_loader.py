import re
from pypdf import PdfReader

def load_document(path):
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def split_text(text, chunk_size=800, overlap=150):
    chunks = []

    paragraphs = text.split("\n")

    current_chunk = ""

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        if len(current_chunk) + len(paragraph) > chunk_size:
            if current_chunk:
                chunks.append(current_chunk.strip())

            current_chunk = current_chunk[-overlap:] + " " + paragraph

        else:
            current_chunk += " " + paragraph

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks
