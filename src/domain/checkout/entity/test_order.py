import pytest

from src.domain.checkout.entity.order import Order
from src.domain.checkout.entity.order_item import OrderItem


class TestOrder:

    # region CREATION
    def test_order_creation_with_success(self):
        # When
        order_item1 = OrderItem("1", "item1", 100, "p1", 2)
        order_item2 = OrderItem("2", "item2", 200, "p2", 2)
        order = Order("1", "1", [order_item1, order_item2])

        # Then
        assert hasattr(order, "id")
        assert hasattr(order, "customer_id")
        assert hasattr(order, "items")
        assert hasattr(order, "total")

        assert order.id == "1"
        assert order.customer_id == "1"
        assert order.items[0].id == "1"
        assert order.items[0].name == "item1"
        assert order.items[0].price == 100
        assert order.items[0].product_id == "p1"
        assert order.items[0].quantity == 2

    def test_order_creation_with_invalid_id(self):
        # When
        order_item1 = OrderItem("1", "item1", 100, "p1", 2)
        order_item2 = OrderItem("2", "item2", 200, "p2", 2)

        # Then
        with pytest.raises(Exception):
            Order("", "1", [order_item1, order_item2])

    def test_order_creation_with_invalid_customer_id(self):
        # When
        order_item1 = OrderItem("1", "item1", 100, "p1", 2)
        order_item2 = OrderItem("2", "item2", 200, "p2", 2)

        # Then
        with pytest.raises(Exception):
            Order("1", "", [order_item1, order_item2])

    def test_order_creation_with_invalid_items(self):
        # When
        order_item1 = OrderItem("1", "item1", 100, "p1", 2)
        order_item2 = OrderItem("2", "item2", 200, "p2", 2)

        # Then
        with pytest.raises(Exception):
            Order("1", "1", [])

    # endregion

    # region TOTAL
    def test_retrieve_total(self):
        # When
        order_item1 = OrderItem("1", "item1", 100, "p1", 2)
        order_item2 = OrderItem("2", "item2", 200, "p2", 2)
        order = Order("1", "1", [order_item1, order_item2])

        # Then
        assert order.total() == 600
    # endregion
