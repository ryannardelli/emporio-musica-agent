import pandas as pd


class ProductRepository:

    def __init__(self):
        self.products = pd.read_csv("data/produtos.csv")

    def search_products(self, name):
        result = self.products[
            self.products["nome"].str.contains(
                name,
                case=False,
                na=False
            )
        ]

        return result.to_dict(orient="records")