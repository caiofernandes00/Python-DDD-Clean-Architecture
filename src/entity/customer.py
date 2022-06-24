from src.entity.address import Address


class Customer:
    def __init__(self, uid: str, name: str, address: Address = None):
        self.__id = uid
        self.__name = name
        self.__active = False

        self.__address: Address = address

        self.validate()

    def validate(self):
        self.__validate_id()
        self.__validate_name()

    def change_name(self, name: str) -> None:
        self.__name = name
        self.__validate_name()

    def change_address(self, address: Address):
        self.__address = address

    def activate(self):
        self.__validate_address()
        self.__active = True

    def deactivate(self):
        self.__active = False

    def __validate_name(self):
        if self.__name.__len__() == 0:
            raise Exception("Name is required")

    def __validate_id(self):
        if self.__id.__len__() == 0:
            raise Exception("Id is required")

    def __validate_address(self):
        if self.__address is None:
            raise Exception("Address is mandatory to activate a customer")
