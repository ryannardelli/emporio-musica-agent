from tools.orders import get_order


def execute_order_flow(order_id, customer_id):
    order = get_order(order_id, customer_id)

    if not order:
        return {
            "success": False,
            "message": "Não encontrei esse pedido."
        }

    return {
        "success": True,
        "data": order
    }