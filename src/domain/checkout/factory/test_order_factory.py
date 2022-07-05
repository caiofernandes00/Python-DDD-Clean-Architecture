from src.domain.checkout.factory.order_factory import OrderFactoryProps, OrderFactoryItemProps, OrderFactory


class TestOrderFactory:

    def test_create_order(self):
        # Arrange
        props = OrderFactoryProps(
            id="1",
            customer_id="1",
            items=[
                OrderFactoryItemProps(
                    id="1",
                    product_id="1",
                    quantity=1,
                    name="name",
                    price=1.0
                )
            ]
        )
        # Act
        order = OrderFactory.create_order(props)
        # Assert
        assert order.id == "1"
        assert order.customer_id == "1"
        assert order.items[0].id == "1"
        assert order.items[0].product_id == "1"
        assert order.items[0].quantity == 1
        assert order.items[0].name == "name"
        assert order.items[0].price == 1.0
        assert order.total() == 1.0
