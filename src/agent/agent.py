from agent.prompts import SYSTEM_PROMPT
from services.llm_service import generate_response

def process_message(message, history):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    messages.extend(history)
    messages.append({"role": "user", "content": message})

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