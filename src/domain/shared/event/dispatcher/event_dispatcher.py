from typing import Dict, List

from src.domain.shared.event.event_dispatcher_interface import EventDispatcherInterface
from src.domain.shared.event.event_handler_interface import EventHandlerInterface
from src.domain.shared.event.event_interface import EventInterface

EventHandlerMappers = Dict[str, List[EventHandlerInterface]]


class EventDispatcher(EventDispatcherInterface):
    def __init__(self):
        self.__event_handlers: Dict[str, List[EventHandlerInterface]] = dict()

    @property
    def event_handlers(self) -> EventHandlerMappers:
        return self.__event_handlers

    def notify(self, event: EventInterface) -> None:
        event_name = type(event).__name__
        if self.__event_handlers.get(event_name):
            for event_handler in self.__event_handlers[event_name]:
                event_handler.handle(event)

    def register(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        if not self.__event_handlers.get(event_name):
            self.__event_handlers[event_name] = []
        self.__event_handlers.get(event_name).append(event_handler)

    def unregister(self, event_name: str, event_handler: EventHandlerInterface) -> None:
        if self.__event_handlers.get(event_name):
            index = self.event_handlers[event_name].index(event_handler)
            del self.__event_handlers[event_name][index]

    def unregister_all(self) -> None:
        self.__event_handlers = dict()
