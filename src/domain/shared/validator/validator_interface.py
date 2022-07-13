from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class ValidatorInterface(ABC, Generic[T]):
    @abstractmethod
    def validate(self, entity) -> None:
        pass
