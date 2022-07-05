from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


class EventInterface(ABC):

    @property
    @abstractmethod
    def data_time_occurred(self) -> datetime:
        pass

    @property
    @abstractmethod
    def event_data(self) -> Any:
        pass
