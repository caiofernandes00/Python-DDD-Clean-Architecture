import pytest

from src.entity.address import Address


class TestAddress:

    # region CREATION
    def test_create_address_with_success(self):
        # When
        address = Address("street", 1, "23123-999", "city")

        # Then
        assert hasattr(address, "street")
        assert hasattr(address, "number")
        assert hasattr(address, "zipcode")
        assert hasattr(address, "city")

        assert address.street == "street"
        assert address.number == 1
        assert address.zipcode == "23123-999"
        assert address.city == "city"

    def test_create_address_with_invalid_street(self):
        # When
        with pytest.raises(Exception):
            Address("", 1, "23123-999", "city")

    def test_create_address_with_invalid_number(self):
        # When
        with pytest.raises(Exception):
            Address("street", 0, "23123-999", "city")
            Address("street", -1, "23123-999", "city")

    def test_create_address_with_invalid_zipcode(self):
        # When
        with pytest.raises(Exception):
            Address("street", 1, "", "city")

    def test_create_address_with_invalid_city(self):
        # When
        with pytest.raises(Exception):
            Address("street", 1, "23123-999", "")

    # endregion
