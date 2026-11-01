from rag.retriever import search_documents

def search_policies(question: str):
    return search_documents(question)