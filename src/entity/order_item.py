class OrderItem:

    def __init__(self, uid: str, name: str, price: int):
        self.__id = uid
        self.__name = name
        self.__price = price

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> int:
        return self.__price
