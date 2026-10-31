import pandas as pd

from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "clientes.csv"


def get_all_customers():
    return pd.read_csv(DATA_PATH)


def get_customer_by_id(customer_id):
    customers = get_all_customers()

    customer = customers[customers["id_cliente"] == customer_id]

    if customer.empty:
        return None

    return customer.iloc[0].to_dict()