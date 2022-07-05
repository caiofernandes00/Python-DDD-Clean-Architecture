from typing import List

from src.domain.product.entity.product import Product


class ProductService:

    @staticmethod
    def increase_price(products: List[Product], percentage: float) -> List[Product]:
        for item in products:
            new_price = item.price + (item.price * percentage / 100)
            item.change_price(new_price)

        return products
