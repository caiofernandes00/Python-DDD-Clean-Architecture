from abc import ABC, abstractmethod

from src.domain.event.shared.event_handler_interface import EventHandlerInterface
from src.domain.event.shared.event_interface import EventInterface


class EventDispatcherInterface(ABC):
    @abstractmethod
    def notify(self, event: EventInterface) -> None:
        pass

    @abstractmethod
    def register(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        pass

    @abstractmethod
    def unregister(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        pass

    @abstractmethod
    def unregister_all(self) -> None:
        pass
