import pytest

from src.infrastructure.customer.repository.peewee.customer_model import CustomerModel
from src.infrastructure.customer.repository.peewee.customer_repository import CustomerRepository
from src.infrastructure.shared.repository.peewee.base_model import sqlite_db
from src.usecase.customer.create.create_customer_dto import OutputCreateCustomerDTO, InputCreateCustomerDTO, \
    InputCreateCustomerAddressDTO
from src.usecase.customer.create.create_customer_usecase import CreateCustomerUseCase


class TestCreateCustomerUseCase:

    @pytest.fixture(autouse=True)
    def setup(self):
        sqlite_db.connect()
        sqlite_db.create_tables([CustomerModel])
        yield
        sqlite_db.drop_tables([CustomerModel])
        sqlite_db.close()

    def test_create_customer(self):
        # Arrange
        address = InputCreateCustomerAddressDTO(street="Street", city="City", number=1, zip="12345")
        input_dto = InputCreateCustomerDTO(name="John Doe", address=address)
        output_dto = OutputCreateCustomerDTO(id="1", name="John Doe", address=address)

        # Act
        customer_repository = CustomerRepository()
        result = CreateCustomerUseCase(customer_repository).execute(input_dto)

        # Assert
        assert hasattr(result, "id")
        assert output_dto.name == result.name
        assert output_dto.address == result.address
