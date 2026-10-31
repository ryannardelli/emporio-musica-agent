from tools.products import search_products


def execute_product_flow(name):
    products = search_products(name)

    if not products:
        return "Não encontrei esse produto em nosso catálogo."

    return products