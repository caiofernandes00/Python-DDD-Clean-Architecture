from abc import ABC

from src.domain.event.shared.event_handler_interface import EventHandlerInterface
from src.domain.event.shared.event_interface import EventInterface


class EventDispatcherInterface(ABC):
    def notify(self, event: EventInterface) -> None:
        pass

    def register(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        pass

    def unregister(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        pass

    def unregister_all(self) -> None:
        pass
