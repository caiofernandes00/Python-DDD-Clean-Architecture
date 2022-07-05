from typing import List

import pytest

from src.domain.customer.value_object.address import Address
from src.domain.customer.entity.customer import Customer
from src.domain.checkout.entity.order import Order
from src.domain.checkout.entity.order_item import OrderItem
from src.domain.product.entity.product import Product
from src.infrastructure.db.peewee.model.base_model import sqlite_db
from src.infrastructure.db.peewee.model.customer_model import CustomerModel as CustomerModel
from src.infrastructure.db.peewee.model.order_item_model import OrderItemModel
from src.infrastructure.db.peewee.model.order_model import OrderModel
from src.infrastructure.db.peewee.model.product_model import ProductModel
from src.infrastructure.repository.order_repository import OrderRepository


class TestOrderRepository:

    @pytest.fixture(autouse=True)
    def setup(self):
        sqlite_db.connect()
        sqlite_db.create_tables([CustomerModel, OrderModel, OrderItemModel, ProductModel])
        yield
        sqlite_db.drop_tables([CustomerModel, OrderModel, OrderItemModel, ProductModel])
        sqlite_db.close()

    @staticmethod
    def create_order() -> Order:
        # CREATE CUSTOMER
        address = Address(street="street", number=1, zipcode="12322-333", city="Atlanta")
        customer = Customer("c1", "fake-name", address)
        CustomerModel.create(id=customer.id, name=customer.name, street=customer.address.street,
                             number=customer.address.number, zipcode=customer.address.zipcode,
                             city=customer.address.city,
                             active=customer.active, reward_points=customer.reward_points)

        # CREATE PRODUCT
        product1 = Product(uid="p1", name="product1", price=100.00)
        product2 = Product(uid="p2", name="product2", price=200.00)
        product1_model = ProductModel(id=product1.id, name=product1.name, price=product1.price)
        product2_model = ProductModel(id=product2.id, name=product2.name, price=product2.price)
        ProductModel.bulk_create([product1_model, product2_model])

        # CREATE ORDER_ITEM
        order_item1 = OrderItem(uid="oi1", product_id="p1", quantity=2, price=100.00, name="product1")
        order_item2 = OrderItem(uid="oi2", product_id="p2", quantity=2, price=200.00, name="product2")

        return Order(uid="o1", customer_id=customer.id, items=[order_item1, order_item2])

    @staticmethod
    def validate_order(order_model: OrderModel):
        assert order_model.id == "o1"
        assert order_model.customer_id == "c1"
        assert order_model.total == 600

    @staticmethod
    def validate_order_item(order_item_models: List[OrderItemModel]):
        assert order_item_models[0].id == "oi1"
        assert order_item_models[0].order_id == "o1"
        assert order_item_models[0].name == "product1"
        assert order_item_models[0].product_id == "p1"
        assert order_item_models[0].quantity == 2
        assert order_item_models[0].price == 100

        assert order_item_models[1].id == "oi2"
        assert order_item_models[1].order_id == "o1"
        assert order_item_models[1].name == "product2"
        assert order_item_models[1].product_id == "p2"
        assert order_item_models[1].quantity == 2
        assert order_item_models[1].price == 200

    def test_inserting(self):
        # When
        order = self.create_order()
        order_repository = OrderRepository()
        order_repository.create(order)

        order_model: OrderModel = OrderModel.get(OrderModel.id == "o1")
        order_item_model: List[OrderItemModel] = OrderItemModel.select().join(OrderModel).where(
            OrderItemModel.order_id == order_model.id)

        # Then
        self.validate_order(order_model)
        self.validate_order_item(order_item_model)

    def test_updating(self):
        # When
        order = self.create_order()
        order_repository = OrderRepository()
        order_repository.create(order)

        order_model: OrderModel = OrderModel.get(OrderModel.id == "o1")
        order_item_model: List[OrderItemModel] = OrderItemModel.select().join(OrderModel).where(
            OrderItemModel.order_id == order_model.id)

        self.validate_order(order_model)
        self.validate_order_item(order_item_model)

        updated_order = order
        updated_order.items[0].change_quantity(4)
        updated_order.items[1].change_quantity(4)

        order_repository.update(updated_order)

        order_model: OrderModel = OrderModel.get(OrderModel.id == "o1")
        order_item_model: List[OrderItemModel] = OrderItemModel.select().join(OrderModel).where(
            OrderItemModel.order_id == order_model.id)

        # Then
        assert updated_order.total() == 1200

        assert order_item_model[0].quantity == 4
        assert order_item_model[0].quantity == 4

    def test_finding_one(self):
        # When
        order = self.create_order()
        order_repository = OrderRepository()
        order_repository.create(order)

        order_returned: Order = order_repository.find(order.id)

        # Then
        assert order_returned.id == order.id
        assert order_returned.total() == order.total()
        assert order_returned.items[0].id == order.items[0].id
        assert order_returned.items[0].name == order.items[0].name
        assert order_returned.items[0].price == order.items[0].price
        assert order_returned.items[0].quantity == order.items[0].quantity
        assert order_returned.items[0].product_id == order.items[0].product_id

        assert order_returned.items[1].id == order.items[1].id
        assert order_returned.items[1].name == order.items[1].name
        assert order_returned.items[1].price == order.items[1].price
        assert order_returned.items[1].quantity == order.items[1].quantity
        assert order_returned.items[1].product_id == order.items[1].product_id

    def test_finding_one_that_dont_exist(self):
        # When
        order_repository = OrderRepository()

        with pytest.raises(Exception):
            order_repository.find("bazinga")

    def test_finding_all(self):
        # When
        order = self.create_order()
        order_repository = OrderRepository()
        order_repository.create(order)

        order_returned: List[Order] = order_repository.find_all()

        # Then
        assert order_returned[0].id == order.id
        assert order_returned[0].total() == order.total()
        assert order_returned[0].items[0].id == order.items[0].id
        assert order_returned[0].items[0].name == order.items[0].name
        assert order_returned[0].items[0].price == order.items[0].price
        assert order_returned[0].items[0].quantity == order.items[0].quantity
        assert order_returned[0].items[0].product_id == order.items[0].product_id

        assert order_returned[0].items[1].id == order.items[1].id
        assert order_returned[0].items[1].name == order.items[1].name
        assert order_returned[0].items[1].price == order.items[1].price
        assert order_returned[0].items[1].quantity == order.items[1].quantity
        assert order_returned[0].items[1].product_id == order.items[1].product_id
