from services.llm_service import generate_response


def main():
    print("=== Empório da Música ===")
    print("Digite 'sair' para encerrar.")

    while True:
        message = input("\nVocê: ")

        if message.lower() == "sair":
            break

        response = generate_response(message)

        print(f"\nAtendente: {response}")


if __name__ == "__main__":
    main()