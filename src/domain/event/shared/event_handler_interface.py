from abc import ABC
from typing import Generic, TypeVar

from src.domain.event.shared.event_interface import EventInterface

T = TypeVar('T', bound=EventInterface)


class EventHandlerInterface(ABC, Generic[T]):
    def handle(self, event: T) -> T:
        pass
