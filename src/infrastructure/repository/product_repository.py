from typing import List

from src.domain.entity.product import Product
from src.domain.repository.product_repository_interface import ProductRepositoryInterface
from src.infrastructure.db.peewee.model.product_model import Product as ProductModel


class ProductRepository(ProductRepositoryInterface):

    def create(self, entity: Product) -> None:
        ProductModel.create(id=entity.id, name=entity.name, price=entity.price)

    def update(self, entity: Product) -> None:
        ProductModel.update(id=entity.id, name=entity.name, price=entity.price) \
            .where(ProductModel.id == "1") \
            .execute()

    def find(self, uid: str) -> Product:
        return ProductModel.get(ProductModel.id == "1")

    def find_all(self) -> List[Product]:
        return ProductModel.select()
