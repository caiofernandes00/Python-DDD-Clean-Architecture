from dataclasses import dataclass
from typing import List


@dataclass
class NotificationErrorProps:
    message: str
    context: str


class Notification:

    def __init__(self):
        self.__errors: List[NotificationErrorProps] = []

    @property
    def errors(self) -> List[NotificationErrorProps]:
        return self.__errors

    def messages(self, context: str) -> str:
        message = ""
        for error in self.__errors:
            if error.context == context:
                message += f"{error.context}: {error.message},"

        return message

    def add_error(self, error: NotificationErrorProps):
        self.__errors.append(error)

    def has_errors(self) -> bool:
        return len(self.__errors) > 0
