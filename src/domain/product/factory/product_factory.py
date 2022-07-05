import uuid

from src.domain.product.entity.product import Product


class ProductFactory:

    @staticmethod
    def create(_type: str, name: str, price: float) -> Product:
        return Product(str(uuid.uuid4()), name, price)
