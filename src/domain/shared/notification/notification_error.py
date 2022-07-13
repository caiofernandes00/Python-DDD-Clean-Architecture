from typing import List

from src.domain.shared.notification.notification import NotificationErrorProps


class NotificationError(Exception):
    def __init__(self, errors: List[NotificationErrorProps]):
        super().__init__(", ".join([error.message for error in errors]))
