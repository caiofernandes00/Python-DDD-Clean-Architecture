from src.domain.customer.factory.customer_factory import CustomerFactory
from src.domain.customer.value_object.address import Address


class TestCustomerFactory:

    def test_create_customer(self):
        # When
        customer = CustomerFactory.create("John")

        # Then
        assert hasattr(customer, "id")
        assert customer.name == "John"
        assert customer.active is False
        assert customer.address is None
        assert customer.reward_points == 0

    def test_create_customer_with_address(self):
        # When
        address = Address("123 Main St", 1, "12345", "CA")
        customer = CustomerFactory.create_with_address("John", address)

        # Then
        assert hasattr(customer, "id")
        assert customer.name == "John"
        assert customer.active is False
        assert customer.address.street == "123 Main St"
        assert customer.reward_points == 0
