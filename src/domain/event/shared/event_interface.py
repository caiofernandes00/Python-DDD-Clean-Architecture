from datetime import datetime
from typing import Any


class EventInterface:
    data_time_occurred: datetime
    event_data: Any
