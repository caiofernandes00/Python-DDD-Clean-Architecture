class OrderItem:

    def __init__(self, uid: str, name: str, price: float):
        self.__id = uid
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

    def validate(self):
        self.__validate_id()
        self.__validate_name()
        self.__validate_price()

    def __validate_id(self) -> None:
        if self.__id.__len__() == 0:
            raise Exception("id is required")

    def __validate_name(self):
        if self.__name.__len__() == 0:
            raise Exception("name is required")

    def __validate_price(self):
        if self.__price < 0:
            raise Exception("price cannot be negative")
