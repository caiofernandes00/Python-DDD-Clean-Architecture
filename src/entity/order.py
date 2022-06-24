from typing import List

from src.entity.order_item import OrderItem


class Order:

    def __init__(self, uid: str, customer_id: str, items: List[OrderItem]):
        self.__id = uid
        self.__customer_id = customer_id
        self.__items = items
