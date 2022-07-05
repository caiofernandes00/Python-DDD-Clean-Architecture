from src.domain.customer.value_object.address import Address


class Customer:
    def __init__(self, uid: str, name: str, address: Address = None) -> None:
        self.__id = uid
        self.__name = name
        self.__active = False
        self.__reward_points: float = 0

        self.__address: Address = address

        self.validate()

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def active(self) -> bool:
        return self.__active

    @property
    def address(self) -> Address:
        return self.__address

    @property
    def reward_points(self):
        return self.__reward_points

    def add_reward_points(self, points: float):
        self.__reward_points += points

    def change_address(self, address: Address) -> None:
        self.__address = address

    def validate(self):
        self.__validate_id()
        self.__validate_name()

    def change_name(self, name: str) -> None:
        self.__name = name
        self.__validate_name()

    def activate(self) -> None:
        self.__validate_address()
        self.__active = True

    def deactivate(self) -> None:
        self.__active = False

    def __validate_name(self) -> None:
        if self.__name is None or self.__name is None or self.__name.__len__() == 0:
            raise Exception("Name is required")

    def __validate_id(self) -> None:
        if self.__id.__len__() == 0:
            raise Exception("Id is required")

    def __validate_address(self) -> None:
        if self.__address is None:
            raise Exception("Address is mandatory to activate a customer")
