from agent.prompts import SYSTEM_PROMPT
from services.llm_service import generate_response


def process_message(message, history):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    messages.extend(history)
    messages.append({"role": "user", "content": message})

    response = generate_response(messages)

    return response.message.content