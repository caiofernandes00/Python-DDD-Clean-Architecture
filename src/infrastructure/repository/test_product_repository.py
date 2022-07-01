from typing import List

import pytest

from src.domain.entity.product import Product
from src.infrastructure.db.peewee.model.base_model import sqlite_db
from src.infrastructure.db.peewee.model.product_model import ProductModel
from src.infrastructure.repository.product_repository import ProductRepository


class TestProductRepository:
    @pytest.fixture(autouse=True)
    def setup(self):
        sqlite_db.connect()
        sqlite_db.create_tables([ProductModel])
        yield
        sqlite_db.drop_tables([ProductModel])
        sqlite_db.close()

    def test_inserting(self):
        # When
        product = Product("1", "fake-name", 100.00)
        product_repository = ProductRepository()
        product_repository.create(product)

        query: ProductModel = ProductModel.get(ProductModel.id == "1")

        # Then
        assert query.id == '1'
        assert query.name == 'fake-name'
        assert query.price == 100.00

    def test_updating(self):
        # When
        product = Product("1", "fake-name", 100.00)
        product_repository = ProductRepository()
        product_repository.create(product)

        query: ProductModel = ProductModel.get(ProductModel.id == "1")

        # Then
        assert query.name == 'fake-name'
        assert query.price == 100.00

        updated_product = Product("1", "fake-name2", 200.00)
        product_repository.update(updated_product)

        query: ProductModel = ProductModel.get(ProductModel.id == "1")

        assert query.name == 'fake-name2'
        assert query.price == 200.00

    def test_finding_one(self):
        # When
        product = Product("1", "fake-name", 100.00)
        product_repository = ProductRepository()
        product_repository.create(product)

        query: Product = product_repository.find('1')

        # Then
        assert query.id == '1'
        assert query.name == 'fake-name'
        assert query.price == 100.00

    def test_finding_one_that_dont_exist(self):
        # When
        product = Product("1", "fake-name", 100.00)
        product_repository = ProductRepository()
        product_repository.create(product)

        with pytest.raises(Exception):
            product_repository.find('2')

    def test_finding_all(self):
        # When
        product = Product("1", "fake-name", 100.00)
        product_repository = ProductRepository()
        product_repository.create(product)

        query: List[Product] = product_repository.find_all()

        # Then
        assert query[0].id == '1'
        assert query[0].name == 'fake-name'
        assert query[0].price == 100.00
