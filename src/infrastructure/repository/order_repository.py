from typing import List

from src.domain.entity.order import Order
from src.domain.entity.order_item import OrderItem
from src.domain.repository.order_repository_interface import OrderRepositoryInterface
from src.infrastructure.db.peewee.model.base_model import sqlite_db
from src.infrastructure.db.peewee.model.order_item_model import OrderItem as OrderItemModel
from src.infrastructure.db.peewee.model.order_model import Order as OrderModel


class OrderRepository(OrderRepositoryInterface):
    def create(self, entity: Order) -> None:
        order_model = OrderModel.create(id=entity.id, customer_id=entity.customer_id, total=entity.total())

        order_items: List[OrderItemModel]
        order_items = [OrderItemModel(id=order_item.id, order_id=order_model.id, product_id=order_item.product_id,
                                      quantity=order_item.quantity, name=order_item.name, price=order_item.price) for
                       order_item in entity.items]

        with sqlite_db.atomic():
            OrderItemModel.bulk_create(order_items, batch_size=10)

    def update(self, entity: Order) -> None:
        OrderModel.update(total=entity.total()) \
            .where(OrderModel.id == entity.id) \
            .execute()

        with sqlite_db.atomic():
            OrderItemModel.bulk_update([x.quantity for x in entity.items], fields=[OrderItem.quantity], batch_size=10)

    def find(self, uid: str) -> Order:
        try:
            order_model = OrderModel.get(OrderModel.id == uid)
            order_item_model = OrderItemModel.select().join(OrderModel).where(OrderModel.id == uid).get()
            return self.__build_entity(order_model, order_item_model)
        except Exception as ex:
            raise Exception("customer not found")

    def find_all(self) -> List[Order]:
        orders: List[Order] = []
        order_models = OrderModel.select()

        for order_model in order_models:
            order_item_model = OrderItemModel.select().join(OrderModel).where(OrderModel.id == order_model.id).get()
            orders.append(self.__build_entity(order_model, order_item_model))

        return orders

    @staticmethod
    def __build_entity(order_model: OrderModel, order_item_model: List[OrderItemModel]) -> Order:
        order_items = [
            OrderItem(uid=order_item.id, name=order_item.name, price=order_item.price, product_id=order_item.product_id,
                      quantity=order_item.quantity)
            for order_item in order_item_model]
        order = Order(uid=order_model.id, customer_id=order_model.customer_id, items=order_items)

        return order
