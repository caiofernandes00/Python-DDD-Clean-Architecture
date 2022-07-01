from typing import List

from src.domain.entity.address import Address
from src.domain.entity.customer import Customer
from src.domain.repository.customer_repository_interface import CustomerRepositoryInterface
from src.infrastructure.db.peewee.model.customer_model import CustomerModel as CustomerModel


class CustomerRepository(CustomerRepositoryInterface):
    def create(self, entity: Customer) -> None:
        CustomerModel.create(id=entity.id, name=entity.name, street=entity.address.street,
                             number=entity.address.number, zipcode=entity.address.zipcode, city=entity.address.city,
                             active=entity.active, reward_points=entity.reward_points)

    def update(self, entity: Customer) -> None:
        CustomerModel.update(name=entity.name, street=entity.address.street,
                             number=entity.address.number, zipcode=entity.address.zipcode, city=entity.address.city,
                             active=entity.active, reward_points=entity.reward_points) \
            .where(CustomerModel.id == entity.id) \
            .execute()

    def find(self, uid: str) -> Customer:
        try:
            customer_model = CustomerModel.get(CustomerModel.id == uid)
            return self.__build_entity(customer_model)
        except Exception as ex:
            raise Exception("customer not found")

    def find_all(self) -> List[Customer]:
        customer_models = CustomerModel.select()
        return list(map(self.__build_entity, customer_models))

    @staticmethod
    def __build_entity(model: CustomerModel) -> Customer:
        customer = Customer(uid=model.id, name=model.name)
        address = Address(street=model.street, number=model.number, zipcode=model.zipcode, city=model.city)
        customer.change_address(address)

        if customer.active:
            customer.activate()

        return customer
