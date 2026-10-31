from src.repositories.product_repository import ProductRepository

repository = ProductRepository()


def search_products(name: str):
    return repository.search_products(name)