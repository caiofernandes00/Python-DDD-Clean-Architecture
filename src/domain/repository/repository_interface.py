from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')


class RepositoryInterface(ABC, Generic[T]):
    @abstractmethod
    def create(self, entity: T) -> None:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def find(self, uid: str) -> T:
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        pass
