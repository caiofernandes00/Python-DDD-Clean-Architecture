import pytest

from src.entity.address import Address
from src.entity.customer import Customer


class TestCustomer:

    # region VALIDATION
    def test_create_customer_with_success(self):
        # When
        customer = Customer("1", "fake-name")

        # Then
        assert hasattr(customer, "id")
        assert hasattr(customer, "name")
        assert hasattr(customer, "address")
        assert hasattr(customer, "reward_points")

        assert customer.id == '1'
        assert customer.name == "fake-name"
        assert customer.address is None

    def test_create_customer_with_success_with_address(self):
        # When
        address = Address("St. Cities Skylines", number=10, zipcode="23232-232", city="Kansas")
        customer = Customer("1", "fake-name", address)

        # Then
        assert hasattr(customer, "id")
        assert hasattr(customer, "name")
        assert hasattr(customer, "address")
        assert hasattr(customer, "reward_points")

        assert customer.id == '1'
        assert customer.name == "fake-name"
        assert customer.address == address

    def test_create_customer_with_invalid_id(self):
        # Then
        with pytest.raises(Exception):
            Customer(uid="", name="fake-name")

    def test_create_customer_with_invalid_name(self):
        # Then
        with pytest.raises(Exception):
            Customer(uid="1", name="")

    # endregion

    # region ACTIVATE CUSTOMER
    def test_activate_customer_with_success(self):
        # When
        address = Address("St. Cities Skylines", number=10, zipcode="23232-232", city="Kansas")
        customer = Customer("1", "fake-name", address)

        # Then
        customer.activate()

    def test_activate_customer_with_error(self):
        # When
        customer = Customer("1", "fake-name")

        # Then
        with pytest.raises(Exception):
            customer.activate()

    # endregion

    # region CHANGING VALUES
    def test_changing_name_with_success(self):
        # When
        customer = Customer("1", "fake-name")

        # Then
        assert customer.name == "fake-name"
        customer.change_name("fake-name2")
        assert customer.name == "fake-name2"

    def test_changing_name_with_error(self):
        # When
        customer = Customer("1", "fake-name")

        # Then
        assert customer.name == "fake-name"
        with pytest.raises(Exception):
            customer.change_name("")

    def test_changing_address_with_success(self):
        # When
        address = Address("St. Cities Skylines", number=10, zipcode="23232-232", city="Kansas")
        customer = Customer("1", "fake-name", address)
        address2 = Address("St. Cities Skylines2", number=11, zipcode="23232-132", city="Mexico")

        # Then
        assert customer.address == address
        customer.address = address2
        assert customer.address == address2

    def test_changing_reward_points_with_success(self):
        # When
        address = Address("St. Cities Skylines", number=10, zipcode="23232-232", city="Kansas")
        customer = Customer("1", "fake-name", address)
        assert customer.reward_points == 0

        customer.add_reward_points(1)

        # Then
        assert customer.reward_points == 1

    # endregion
