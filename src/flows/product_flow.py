from tools.products import search_products


def execute_product_flow(product_name):
    products = search_products(product_name)

    if not products:
        return {
            "success": False,
            "message": "Não encontrei esse produto no catálogo."
        }

    return {
        "success": True,
        "data": products
    }