class OrderItem:

    def __init__(self, uid: str, name: str, price: float, product_id: str, quantity: int):
        self.__id = uid
        self.__product_id = product_id
        self.__quantity = quantity
        self.__name = name
        self.__price = price
        self.validate()

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def product_id(self):
        return self.__product_id

    @property
    def quantity(self) -> int:
        return self.__quantity

    def change_quantity(self, new_amount: int):
        self.__quantity = new_amount

    def validate(self):
        self.__validate_id()
        self.__validate_name()
        self.__validate_price()
        self.__validate_product_id()
        self.__validate_quantity()

    def __validate_id(self) -> None:
        if self.__id.__len__() == 0:
            raise Exception("id is required")

    def __validate_name(self):
        if self.__name.__len__() == 0:
            raise Exception("name is required")

    def __validate_price(self):
        if self.__price < 0:
            raise Exception("price cannot be negative")

    def __validate_product_id(self):
        if self.__product_id.__len__() == 0:
            raise Exception("product_id is required")

    def __validate_quantity(self) -> None:
        if self.__quantity < 1:
            raise Exception("quantity should be greater than zero")
