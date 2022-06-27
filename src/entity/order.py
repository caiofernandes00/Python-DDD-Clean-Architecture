from typing import List

from src.entity.order_item import OrderItem


class Order:

    def __init__(self, uid: str, customer_id: str, items: List[OrderItem]):
        self.__id = uid
        self.__customer_id = customer_id
        self.__items = items
        self.validate()
        self.__total = self.total()

    @property
    def id(self) -> str:
        return self.__id

    @property
    def customer_id(self) -> str:
        return self.__customer_id

    @property
    def items(self) -> List[OrderItem]:
        return self.__items

    def total(self) -> int:
        total = 0
        for item in self.__items:
            total += (item.price * item.quantity)

        return total

    def validate(self):
        self.__validate_id()
        self.__validate_customer_id()
        self.__validate_items()

    def __validate_id(self) -> None:
        if self.__id.__len__() == 0:
            raise Exception("id is required")

    def __validate_customer_id(self) -> None:
        if self.__customer_id.__len__() == 0:
            raise Exception("customer_id is required")

    def __validate_items(self) -> None:
        if self.__items.__len__() == 0:
            raise Exception("items is required")
