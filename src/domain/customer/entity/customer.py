from src.domain.customer.value_object.address import Address
from src.domain.shared.entity.entity_abstract import Entity
from src.domain.shared.notification.notification import NotificationErrorProps
from src.domain.shared.notification.notification_error import NotificationError


class Customer(Entity):
    def __init__(self, uid: str, name: str, address: Address = None) -> None:
        super().__init__(uid)
        self.__name = name
        self.__active = False
        self.__reward_points: float = 0

        self.__address: Address = address

        self.validate()

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

        if self._notification.has_errors():
            raise NotificationError(self._notification.errors)

    def change_name(self, name: str) -> None:
        self.__name = name
        self.__validate_name()
        if self._notification.has_errors():
            raise NotificationError(self._notification.errors)

    def activate(self) -> None:
        self.__validate_address()
        self.__active = True
        if self._notification.has_errors():
            raise NotificationError(self._notification.errors)

    def deactivate(self) -> None:
        self.__active = False

    def __validate_name(self) -> None:
        if self.__name is None or self.__name is None or self.__name.__len__() == 0:
            error = NotificationErrorProps(message="Customer name is required", context=type(self).__name__)
            self._notification.add_error(error)

    def __validate_id(self) -> None:
        if self.id.__len__() == 0:
            error = NotificationErrorProps(message="Customer id is required", context=type(self).__name__)
            self._notification.add_error(error)

    def __validate_address(self) -> None:
        if self.__address is None:
            error = NotificationErrorProps(message="Customer address is required", context=type(self).__name__)
            self._notification.add_error(error)
