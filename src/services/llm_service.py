import os
import ollama

from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL")
HOST = os.getenv("OLLAMA_HOST")

client = ollama.Client(host=HOST)


def generate_response(message):
    response = client.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
                    Você é o assistente virtual da Empório da Música,
                    uma loja de instrumentos musicais localizada em Campo Grande/MS.

                    Seja educado, cordial e prestativo.
                    Responda em português brasileiro.
                """
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.message.content