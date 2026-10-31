import pandas as pd

class OrderRepository:

    def __init__(self):
        self.orders = pd.read_csv("data/pedidos.csv")

    def get_order(self, order_id, customer_id):
        result = self.orders[
            (self.orders["id"] == order_id) &
            (self.orders["cliente_id"] == customer_id)
        ]

        if result.empty:
            return None

        return result.to_dict(orient="records")[0]