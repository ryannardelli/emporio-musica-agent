import pandas as pd

from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "promocoes.csv"


def get_all_promotions():
    return pd.read_csv(DATA_PATH)


def get_promotion_by_id(promotion_id):
    promotions = get_all_promotions()

    promotion = promotions[promotions["id_promocao"] == promotion_id]

    if promotion.empty:
        return None

    return promotion.iloc[0].to_dict()