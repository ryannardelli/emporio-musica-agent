from agent.prompts import SYSTEM_PROMPT
from services.llm_service import generate_response
from rag.retriever import search_documents
from tools.products import PRODUCT_FUNCTIONS
from tools.tool_definitions import PRODUCT_TOOLS

import json

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

    print("\nO atendente está digitando...", end="", flush=True)

    response = generate_response(
        messages,
        tools=PRODUCT_TOOLS
    )

    tool_calls = []
    full_response = ""

    for chunk in response:
        if chunk.message.tool_calls:
            tool_calls.extend(chunk.message.tool_calls)

        if chunk.message.content:
            full_response += chunk.message.content

    if tool_calls:
        messages.append({
            "role": "assistant",
            "tool_calls": tool_calls
        })

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            function = PRODUCT_FUNCTIONS.get(function_name)

            if function:
                result = function(**arguments)
            else:
                result = {"erro": "Ferramenta não encontrada."}

            messages.append({
                "role": "tool",
                "content": json.dumps(result, ensure_ascii=False)
            })

        response = generate_response(messages)

        full_response = ""
        first_chunk = True

        for chunk in response:
            content = chunk.message.content

            if content:
                if first_chunk:
                    print("\rAtendente: ", end="", flush=True)
                    first_chunk = False

                print(content, end="", flush=True)
                full_response += content

    else:
        print("\rAtendente: ", end="", flush=True)
        print(full_response, end="", flush=True)

    print()

    return full_response