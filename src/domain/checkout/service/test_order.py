from src.domain.customer.entity.customer import Customer
from src.domain.checkout.entity.order import Order
from src.domain.checkout.entity.order_item import OrderItem
from src.domain.checkout.service.order_service import OrderService


class TestOrder:

    def test_should_get_total_of_orders(self):
        # Arrange
        order_item1 = OrderItem("1", "item1", 100, "p1", 1)
        order_item2 = OrderItem("2", "item2", 200, "p2", 2)

        order1 = Order("o1", "c1", [order_item1])
        order2 = Order("o2", "c2", [order_item2])

        # When
        total = OrderService.total([order1, order2])

        # Then
        assert total == 500

    def test_should_place_an_order(self):
        # Arrange
        customer = Customer("c1", "Customer 1")
        order_item = OrderItem("i1", "Item 1", 10, "p1", 1)

        # When
        order = OrderService.place_order(customer, [order_item])

        # Then
        assert customer.reward_points == 5
        assert order.total() == 10
