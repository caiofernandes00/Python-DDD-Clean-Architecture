from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.domain.shared.event.event_interface import EventInterface

T = TypeVar('T', bound=EventInterface)


class EventHandlerInterface(ABC, Generic[T]):

    @abstractmethod
    def handle(self, event: T) -> None:
        pass
