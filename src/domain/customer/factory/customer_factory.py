import uuid

from src.domain.customer.entity.customer import Customer
from src.domain.customer.value_object.address import Address


class CustomerFactory:

    @staticmethod
    def create(name: str) -> Customer:
        return Customer(str(uuid.uuid4()), name)

    @staticmethod
    def create_with_address(name: str, address: Address) -> Customer:
        return Customer(str(uuid.uuid4()), name, address)
