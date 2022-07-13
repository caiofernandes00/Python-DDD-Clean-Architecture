from src.domain.customer.factory.customer_validator_factory import CustomerValidatorFactory
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

    def validate(self) -> None:
        CustomerValidatorFactory.create().validate(self)
        if self.notification.has_errors():
            raise NotificationError(self.notification.errors)

    def change_name(self, name: str) -> None:
        self.__name = name
        CustomerValidatorFactory.create().validate(self)
        if self.notification.has_errors():
            raise NotificationError(self.notification.errors)

    def activate(self) -> None:
        if self.__address is None:
            raise NotificationError(
                [NotificationErrorProps(message="Customer address is required", context=type(self).__name__)])
        self.__active = True

    def deactivate(self) -> None:
        self.__active = False
