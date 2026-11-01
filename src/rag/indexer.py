from pathlib import Path

from rag.document_loader import load_document, split_text
from rag.retriever import index_documents

PDF_PATH = Path(__file__).resolve().parents[2] / "data" / "politicas_da_loja.pdf"

def index_policies():
    text = load_document(PDF_PATH)

    chunks = split_text(text)

    index_documents(chunks)