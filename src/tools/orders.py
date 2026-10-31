from src.repositories.order_repository import OrderRepository

repository = OrderRepository()


def get_order(order_id: int, customer_id: int):
    return repository.get_order(order_id, customer_id)