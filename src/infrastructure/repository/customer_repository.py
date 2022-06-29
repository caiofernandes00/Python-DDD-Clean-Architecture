from typing import List

from src.domain.entity.customer import Customer
from src.domain.repository.customer_repository_interface import CustomerRepositoryInterface
from src.infrastructure.db.peewee.model.customer_model import Customer as CustomerModel


class CustomerRepository(CustomerRepositoryInterface):
    def create(self, entity: Customer) -> None:
        CustomerModel.create(id=entity.id, name=entity.name, street=entity.address.street,
                             numbers=entity.address.number, zipcode=entity.address.zipcode, city=entity.address.city,
                             active=entity.active, reward_points=entity.reward_points)

    def update(self, entity: Customer) -> None:
        CustomerModel.update(name=entity.name, street=entity.address.street,
                             numbers=entity.address.number, zipcode=entity.address.zipcode, city=entity.address.city,
                             active=entity.active, reward_points=entity.reward_points) \
            .where(CustomerModel.id == "1") \
            .execute()

    def find(self, uid: str) -> Customer:
        return CustomerModel.get(CustomerModel.id == "1")

    def find_all(self) -> List[Customer]:
        return CustomerModel.select()
