import dataclasses
from dataclasses import dataclass
from typing import List

from src.domain.checkout.entity.order import Order
from src.domain.checkout.entity.order_item import OrderItem


@dataclass
class OrderFactoryItemProps:
    id: str
    product_id: str
    quantity: int
    name: str
    price: float


@dataclass
class OrderFactoryProps:
    id: str
    customer_id: str
    items: List[OrderFactoryItemProps]


class OrderFactory:

    @staticmethod
    def create_order(props: OrderFactoryProps) -> Order:
        order_items = []
        for item in props.items:
            dict_item = dataclasses.asdict(item)
            order_items.append(OrderItem(
                uid=dict_item['id'],
                product_id=dict_item['product_id'],
                quantity=dict_item['quantity'],
                name=dict_item['name'],
                price=dict_item['price']
            ))
        return Order(props.id, props.customer_id, order_items)
