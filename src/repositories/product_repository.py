from pathlib import Path

import pandas as pd


class ProductRepository:
    def __init__(self):
        csv_path = Path(__file__).resolve().parents[2] / "data" / "products.csv"
        self.products = pd.read_csv(csv_path)

    def search_products(self, name):
        result = self.products[
            self.products["name"].str.contains(
                name,
                case=False,
                na=False
            )
        ]

        return result.to_dict(orient="records")

    def get_products_by_max_price(self, max_price):
        result = self.products[
            (self.products["price_brl"] <= max_price) &
            (self.products["stock_quantity"] > 0)
        ]

        return result.to_dict(orient="records")

    def get_product_by_name(self, name):
        result = self.products[
            self.products["name"].str.contains(
                name,
                case=False,
                na=False
            )
        ]

        if result.empty:
            return None

        return result.iloc[0].to_dict()
