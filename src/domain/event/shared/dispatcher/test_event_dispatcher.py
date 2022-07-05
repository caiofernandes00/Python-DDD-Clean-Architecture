from src.domain.entity.product import Product
from src.domain.event.product.handler.send_email_when_product_is_created_handler import \
    SendEmailWhenProductIsCreatedHandler
from src.domain.event.product.product_created_event import ProductCreatedEvent
from src.domain.event.shared.dispatcher.event_dispatcher import EventDispatcher


class TestEventDispatcher:

    def test_register_an_event(self):
        # When
        event_dispatcher = EventDispatcher()
        event_handler = SendEmailWhenProductIsCreatedHandler()

        event_dispatcher.register("ProductCreatedEvent", event_handler)

        # Then
        assert len(event_dispatcher.event_handlers) == 1
        assert len(event_dispatcher.event_handlers['ProductCreatedEvent']) == 1
        assert event_dispatcher.event_handlers["ProductCreatedEvent"] == [event_handler]

    def test_unregister_an_event(self):
        # When
        event_dispatcher = EventDispatcher()
        event_handler = SendEmailWhenProductIsCreatedHandler()

        event_dispatcher.register("ProductCreatedEvent", event_handler)
        assert len(event_dispatcher.event_handlers) == 1
        assert len(event_dispatcher.event_handlers['ProductCreatedEvent']) == 1
        assert event_dispatcher.event_handlers["ProductCreatedEvent"] == [event_handler]

        event_dispatcher.unregister("ProductCreatedEvent", event_handler)

        # Then
        assert len(event_dispatcher.event_handlers) == 1
        assert len(event_dispatcher.event_handlers['ProductCreatedEvent']) == 0
        assert event_dispatcher.event_handlers["ProductCreatedEvent"] == []

    def test_unregister_all_events(self):
        # When
        event_dispatcher = EventDispatcher()
        event_handler = SendEmailWhenProductIsCreatedHandler()

        event_dispatcher.register("ProductCreatedEvent", event_handler)
        assert len(event_dispatcher.event_handlers) == 1
        assert len(event_dispatcher.event_handlers['ProductCreatedEvent']) == 1
        assert event_dispatcher.event_handlers["ProductCreatedEvent"] == [event_handler]

        event_dispatcher.unregister_all()

        # Then
        assert len(event_dispatcher.event_handlers) == 0
        assert event_dispatcher.event_handlers == {}

    def test_notify_an_event(self, mocker):
        # When
        event_dispatcher = EventDispatcher()
        event_handler = SendEmailWhenProductIsCreatedHandler()

        event_dispatcher.register("ProductCreatedEvent", event_handler)
        assert len(event_dispatcher.event_handlers) == 1
        assert len(event_dispatcher.event_handlers['ProductCreatedEvent']) == 1
        assert event_dispatcher.event_handlers["ProductCreatedEvent"] == [event_handler]

        created_event = ProductCreatedEvent(event_date=Product(uid="1", name="Product 1", price=10.0))

        # Then
        # spy = mocker.spy(event_handler, 'handle')
        # assert spy.assert_called_once_with(created_event)
        event_dispatcher.notify(created_event)
