from datetime import datetime
from typing import Any

from src.domain.event.shared.event_interface import EventInterface


class ProductCreatedEvent(EventInterface):
    def __init__(self, data_time_occurred: datetime, event_date: Any):
        self.__data_time_occurred = data_time_occurred
        self.__event_data = event_date

    def data_time_occurred(self) -> datetime:
        return self.__data_time_occurred

    def event_data(self) -> Any:
        return self.__event_data
