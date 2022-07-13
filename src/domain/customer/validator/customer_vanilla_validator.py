from typing import Any

from src.domain.shared.notification.notification import NotificationErrorProps
from src.domain.shared.validator.validator_interface import ValidatorInterface


# This class could use some validator library
class CustomerVanillaValidator(ValidatorInterface):

    def validate(self, entity: Any) -> None:
        self.__validate_id(entity)
        self.__validate_name(entity)

    def __validate_name(self, entity: Any) -> None:
        if entity.name is None or entity.name is None or entity.name.__len__() == 0:
            error = NotificationErrorProps(message="Customer name is required", context=type(self).__name__)
            entity.notification.add_error(error)

    def __validate_id(self, entity: Any) -> None:
        if entity.id.__len__() == 0:
            error = NotificationErrorProps(message="Customer id is required", context=type(self).__name__)
            entity.notification.add_error(error)

    def __validate_address(self, entity: Any) -> None:
        if entity.address is None:
            error = NotificationErrorProps(message="Customer address is required", context=type(self).__name__)
            entity.notification.add_error(error)
