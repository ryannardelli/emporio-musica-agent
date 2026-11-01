from agent.prompts import SYSTEM_PROMPT
from services.llm_service import generate_response
from rag.retriever import search_documents


def process_message(message, history):
    context = search_documents(message)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    messages.extend(history)

    messages.append({
        "role": "user",
        "content": f"""
            Pergunta do cliente:
            {message}

            Contexto encontrado nas políticas da loja:
            {context}

            Utilize o contexto quando ele for relevante para responder.
            Não invente informações que não estejam disponíveis.
        """
    })

    response = generate_response(messages)

    full_response = ""
    first_chunk = True

    print("\nO atendente está digitando...", end="", flush=True)

    for chunk in response:
        content = chunk.message.content

        if content:
            if first_chunk:
                print("\rAtendente: ", end="", flush=True)
                first_chunk = False

            print(content, end="", flush=True)
            full_response += content

    print()

    return full_response