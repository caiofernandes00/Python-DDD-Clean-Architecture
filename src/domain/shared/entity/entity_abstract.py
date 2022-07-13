from src.domain.shared.notification.notification import Notification


class Entity:
    def __init__(self, uid: str):
        self.__id: str = uid
        self.__notification = Notification()

    @property
    def id(self) -> str:
        return self.__id

    @property
    def notification(self):
        return self.__notification
