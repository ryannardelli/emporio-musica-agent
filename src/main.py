from agent.agent import process_message


def main():
    history = []

    print("=== Empório da Música ===")
    print("Digite 'sair' para encerrar.")

    while True:
        message = input("\nVocê: ")

        if message.lower() == "sair":
            break

        response = process_message(message, history)

        print(f"\nAtendente: {response}")


if __name__ == "__main__":
    main()