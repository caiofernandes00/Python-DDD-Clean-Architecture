from typing import List

from src.domain.product.entity.product import Product
from src.domain.product.repository.product_repository_interface import ProductRepositoryInterface
from src.infrastructure.db.peewee.model.product_model import ProductModel


class ProductRepository(ProductRepositoryInterface):

    def create(self, entity: Product) -> None:
        ProductModel.create(id=entity.id, name=entity.name, price=entity.price)

    def update(self, entity: Product) -> None:
        ProductModel.update(name=entity.name, price=entity.price) \
            .where(ProductModel.id == entity.id) \
            .execute()

    def find(self, uid: str) -> Product:
        try:
            return ProductModel.get(ProductModel.id == uid)
        except Exception as ex:
            raise Exception("product not found")

    def find_all(self) -> List[Product]:
        return ProductModel.select()
