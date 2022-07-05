import pytest

from src.domain.customer.entity.customer import Customer
from src.domain.customer.value_object.address import Address
from src.infrastructure.customer.repository.peewee.customer_model import CustomerModel
from src.infrastructure.customer.repository.peewee.customer_repository import CustomerRepository
from src.infrastructure.shared.repository.peewee.base_model import sqlite_db
from src.usecase.customer.find.find_customer_dto import InputFindCustomerDTO, OutputFindCustomerDTO, \
    OutputFindCustomerAddressDTO
from src.usecase.customer.find.find_customer_usecase import FindCustomerUseCase


class TestFindCustomer:
    @pytest.fixture(autouse=True)
    def setup(self):
        sqlite_db.connect()
        sqlite_db.create_tables([CustomerModel])
        yield
        sqlite_db.drop_tables([CustomerModel])
        sqlite_db.close()

    def test_find_customer(self):
        # Arrange
        input_dto = InputFindCustomerDTO(id="1")
        output_dto = OutputFindCustomerDTO(id="1", name="John Doe",
                                           address=OutputFindCustomerAddressDTO(street="Street", city="City", number=1,
                                                                                zip="12345"))

        address = Address('Street', 1, '12345', 'City')
        customer = Customer("1", "John Doe", address)
        CustomerModel.create(id=customer.id, name=customer.name, street=customer.address.street,
                             number=customer.address.number, zipcode=customer.address.zipcode,
                             city=customer.address.city, active=customer.active, reward_points=customer.reward_points)

        # Act
        customer_repository = CustomerRepository()
        result = FindCustomerUseCase(customer_repository).execute(input_dto)

        # Assert
        assert output_dto.id == result.id
        assert output_dto.name == result.name
        assert output_dto.address.street == result.address.street
        assert output_dto.address.number == result.address.number
        assert output_dto.address.zip == result.address.zip
        assert output_dto.address.city == result.address.city

    def test_not_find_customer(self):
        # Arrange
        input_dto = InputFindCustomerDTO(id="2")
        output_dto = OutputFindCustomerDTO(id="1", name="John Doe",
                                           address=OutputFindCustomerAddressDTO(street="Street", city="City", number=1,
                                                                                zip="12345"))

        address = Address('Street', 1, '12345', 'City')
        customer = Customer("1", "John Doe", address)
        CustomerModel.create(id=customer.id, name=customer.name, street=customer.address.street,
                             number=customer.address.number, zipcode=customer.address.zipcode,
                             city=customer.address.city, active=customer.active, reward_points=customer.reward_points)

        # Act
        customer_repository = CustomerRepository()

        # Assert
        with pytest.raises(Exception):
            FindCustomerUseCase(customer_repository).execute(input_dto)
