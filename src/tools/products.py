from repositories.product_repository import ProductRepository

repository = ProductRepository()


def search_products(name: str):
    return repository.search_products(name)


def get_products_by_max_price(max_price: float):
    return repository.get_products_by_max_price(max_price)


def get_product_by_name(name: str):
    return repository.get_product_by_name(name)

PRODUCT_FUNCTIONS = {
    "search_products": search_products,
    "get_products_by_max_price": get_products_by_max_price,
    "get_product_by_name": get_product_by_name
}