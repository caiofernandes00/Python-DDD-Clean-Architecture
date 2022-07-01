import uuid
from typing import List

from src.domain.entity.customer import Customer
from src.domain.entity.order import Order
from src.domain.entity.order_item import OrderItem


class OrderService:
    @staticmethod
    def place_order(customer: Customer, items: List[OrderItem]) -> Order:
        if len(items) == 0:
            raise Exception("OrderModel must have at least one item")

        order = Order(str(uuid.uuid4()), customer.id, items)
        customer.add_reward_points(order.total() / 2)
        return order

    @staticmethod
    def total(orders: List[Order]) -> float:
        total: float = 0.00
        for order in orders:
            total += order.total()

        return total
