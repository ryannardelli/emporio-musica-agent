import os
import ollama

from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL")
HOST = os.getenv("OLLAMA_HOST")

client = ollama.Client(host=HOST)


def generate_response(messages, tools=None):
    response = client.chat(
        model=MODEL,
        messages=messages,
        tools=tools or []
    )

    return response