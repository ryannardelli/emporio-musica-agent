from pypdf import PdfReader


def load_document(path):
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text