from src.repositories.promotion_repository import PromotionRepository

repository = PromotionRepository()


def search_promotions():
    return repository.get_active_promotions()