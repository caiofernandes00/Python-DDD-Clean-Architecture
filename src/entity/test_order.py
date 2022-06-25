import pytest

from src.entity.order import Order
from src.entity.order_item import OrderItem


class TestOrder:

    # region CREATION
    def test_order_creation_with_success(self):
        # When
        order_item1 = OrderItem("1", "item1", 100)
        order_item2 = OrderItem("2", "item2", 200)
        order = Order("1", "1", [order_item1, order_item2])

        # Then
        assert hasattr(order, "_Order__id")
        assert hasattr(order, "_Order__customer_id")
        assert hasattr(order, "_Order__total")

        assert order.id == "1"
        assert order.customer_id == "1"
        assert order.items[0].name == "item1"

    def test_order_creation_with_invalid_id(self):
        # When
        order_item1 = OrderItem("1", "item1", 100)
        order_item2 = OrderItem("2", "item2", 200)

        # Then
        with pytest.raises(Exception):
            Order("", "1", [order_item1, order_item2])

    def test_order_creation_with_invalid_customer_id(self):
        # When
        order_item1 = OrderItem("1", "item1", 100)
        order_item2 = OrderItem("2", "item2", 200)

        # Then
        with pytest.raises(Exception):
            Order("1", "", [order_item1, order_item2])

    def test_order_creation_with_invalid_items(self):
        # When
        order_item1 = OrderItem("1", "item1", 100)
        order_item2 = OrderItem("2", "item2", 200)

        # Then
        with pytest.raises(Exception):
            Order("1", "1", [])

    # endregion

    # region TOTAL
    def test_retrieve_total(self):
        # When
        order_item1 = OrderItem("1", "item1", 100)
        order_item2 = OrderItem("2", "item2", 200)
        order = Order("1", "1", [order_item1, order_item2])

        # Then
        assert order.total() == 300
    # endregion
