from tools.policies import search_policies


def execute_policy_flow(question):
    context = search_policies(question)

    if not context:
        return {
            "success": False,
            "message": "Não encontrei informações sobre essa política."
        }

    return {
        "success": True,
        "data": context
    }