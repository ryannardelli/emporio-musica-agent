from tools.promotions import search_promotions


def execute_promotion_flow():
    promotions = search_promotions()

    return {
        "success": True,
        "data": promotions
    }