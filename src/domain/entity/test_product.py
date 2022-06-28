import pytest

from src.domain.entity.product import Product


class TestProduct:

    # region CREATION
    def test_create_product_with_success(self):
        # When
        product = Product("1", "name", 100.00)

        # Then
        assert hasattr(product, "id")
        assert hasattr(product, "name")
        assert hasattr(product, "price")

        assert product.id == "1"
        assert product.name == "name"
        assert product.price == 100.00

    def test_create_product_with_invalid_id(self):
        # When
        with pytest.raises(Exception):
            Product("", "name", 100.00)

    def test_create_product_with_invalid_name(self):
        # When
        with pytest.raises(Exception):
            Product("1", "", 100.00)

    def test_create_product_with_invalid_price(self):
        # When
        with pytest.raises(Exception):
            Product("1", "name", -100.00)

    # endregion

    # region UPDATE
    def test_update_name_with_success(self):
        # When
        product = Product("1", "name", 100.00)
        product.change_name("name2")

        # Then
        assert product.name == "name2"

    def test_update_name_with_invalid_name(self):
        # When
        product = Product("1", "name", 100.00)
        with pytest.raises(Exception):
            product.change_name("")

    def test_update_name_with_invalid_price(self):
        # When
        product = Product("1", "name", 100.00)
        with pytest.raises(Exception):
            product.change_price(-1)

    # endregion
