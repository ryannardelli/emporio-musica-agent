import os
import ollama
import chromadb

from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL")

client = ollama.Client()

chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="store_policies"
)


def generate_embedding(text):
    response = client.embed(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response["embeddings"][0]


def index_documents(chunks):
    for index, chunk in enumerate(chunks):
        embedding = generate_embedding(chunk)

        collection.add(
            ids=[str(index)],
            documents=[chunk],
            embeddings=[embedding]
        )


def search_documents(query, n_results=3):
    embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    return results["documents"][0]