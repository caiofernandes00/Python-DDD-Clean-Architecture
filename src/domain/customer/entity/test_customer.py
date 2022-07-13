import pytest

from src.domain.customer.entity.customer import Customer
from src.domain.customer.value_object.address import Address
from src.domain.shared.notification.notification_error import NotificationError


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
        with pytest.raises(NotificationError) as ex:
            Customer(uid="", name="fake-name")

        assert ex.value.args[0] == "Customer id is required"

    def test_create_customer_with_invalid_name(self):
        # Then
        with pytest.raises(NotificationError) as ex:
            Customer(uid="1", name="")

        assert ex.value.args[0] == "Customer name is required"

    def test_create_customer_with_many_errors(self):
        # Then
        with pytest.raises(NotificationError) as ex:
            Customer(uid="", name="")

        errors = ex.value.args[0].split(", ")
        assert errors[0] == "Customer id is required"
        assert errors[1] == 'Customer name is required'

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
        with pytest.raises(NotificationError) as ex:
            customer.activate()

        assert ex.value.args[0] == "Customer address is required"

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
        with pytest.raises(NotificationError) as ex:
            customer.change_name("")

        assert ex.value.args[0] == "Customer name is required"

    def test_changing_address_with_success(self):
        # When
        address = Address("St. Cities Skylines", number=10, zipcode="23232-232", city="Kansas")
        customer = Customer("1", "fake-name", address)
        address2 = Address("St. Cities Skylines2", number=11, zipcode="23232-132", city="Mexico")

        # Then
        assert customer.address == address
        customer.change_address(address2)
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
