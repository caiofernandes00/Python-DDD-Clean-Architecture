import pytest

from src.entity.order_item import OrderItem


class TestOrderItem:

    # region CREATION
    def test_create_order_item_with_success(self):
        # When
        order_item = OrderItem("1", "item1", 100.00, "p1", 2)

        # Then
        assert hasattr(order_item, "id")
        assert hasattr(order_item, "name")
        assert hasattr(order_item, "price")

        assert order_item.id == "1"
        assert order_item.name == "item1"
        assert order_item.price == 100.00

    def test_create_order_item_with_invalid_id(self):
        # Then
        with pytest.raises(Exception):
            OrderItem("", "item1", 100.00, "p1", 2)

    def test_create_order_item_with_invalid_name(self):
        # Then
        with pytest.raises(Exception):
            OrderItem("1", "", 100.00, "p1", 2)

    def test_create_order_item_with_invalid_price(self):
        # Then
        with pytest.raises(Exception):
            OrderItem("1", "item1", -100.00, "p1", 2)

    def test_create_order_item_with_invalid_product_id(self):
        # Then
        with pytest.raises(Exception):
            OrderItem("1", "item1", -100.00, "", 2)

    def test_create_order_item_with_invalid_quantity(self):
        # Then
        with pytest.raises(Exception):
            OrderItem("1", "item1", -100.00, "p1", -2)
    # endregion
