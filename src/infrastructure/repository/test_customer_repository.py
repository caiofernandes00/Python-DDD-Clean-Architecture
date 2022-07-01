from typing import List

import pytest

from src.domain.entity.address import Address
from src.domain.entity.customer import Customer
from src.infrastructure.db.peewee.model.base_model import sqlite_db
from src.infrastructure.db.peewee.model.customer_model import CustomerModel
from src.infrastructure.repository.customer_repository import CustomerRepository


class TestCustomerRepository:
    @pytest.fixture(autouse=True)
    def setup(self):
        sqlite_db.connect()
        sqlite_db.create_tables([CustomerModel])
        yield
        sqlite_db.drop_tables([CustomerModel])
        sqlite_db.close()

    def test_inserting(self):
        # When
        address = Address(street="street", number=1, zipcode="12322-333", city="Atlanta")
        customer = Customer("1", "fake-name", address)
        customer_repository = CustomerRepository()
        customer_repository.create(customer)

        query: CustomerModel = CustomerModel.get(CustomerModel.id == "1")

        # Then
        assert query.id == '1'
        assert query.name == 'fake-name'
        assert query.street == 'street'
        assert query.number == 1
        assert query.zipcode == '12322-333'
        assert query.city == 'Atlanta'
        assert query.active is False
        assert query.reward_points == 0

    def test_updating(self):
        # When
        address = Address(street="street", number=1, zipcode="12322-333", city="Atlanta")
        customer = Customer("1", "fake-name", address)
        customer_repository = CustomerRepository()
        customer_repository.create(customer)

        query: CustomerModel = CustomerModel.get(CustomerModel.id == "1")

        # Then
        assert query.id == '1'
        assert query.name == 'fake-name'

        address = Address(street="street2", number=1, zipcode="12322-333", city="Atlanta")
        updated_customer = Customer("1", "fake-name2", address)
        customer_repository.update(updated_customer)

        query: CustomerModel = CustomerModel.get(CustomerModel.id == "1")

        assert query.id == '1'
        assert query.name == 'fake-name2'
        assert query.street == 'street2'

    def test_finding_one(self):
        # When
        address = Address(street="street", number=1, zipcode="12322-333", city="Atlanta")
        customer = Customer("1", "fake-name", address)
        customer_repository = CustomerRepository()
        customer_repository.create(customer)

        query: Customer = customer_repository.find('1')

        # Then
        assert query.id == '1'
        assert query.name == 'fake-name'
        assert query.address.street == 'street'
        assert query.address.number == 1
        assert query.address.zipcode == '12322-333'
        assert query.address.city == 'Atlanta'
        assert query.active is False
        assert query.reward_points == 0

    def test_finding_one_that_dont_exist(self):
        # When
        customer_repository = CustomerRepository()

        with pytest.raises(Exception):
            customer_repository.find('2')

    def test_finding_all(self):
        # When
        address = Address(street="street", number=1, zipcode="12322-333", city="Atlanta")
        customer = Customer("1", "fake-name", address)
        customer_repository = CustomerRepository()
        customer_repository.create(customer)

        query: List[Customer] = customer_repository.find_all()

        # Then
        assert query[0].id == '1'
        assert query[0].name == 'fake-name'
        assert query[0].address.street == 'street'
        assert query[0].address.number == 1
        assert query[0].address.zipcode == '12322-333'
        assert query[0].address.city == 'Atlanta'
        assert query[0].active is False
        assert query[0].reward_points == 0
