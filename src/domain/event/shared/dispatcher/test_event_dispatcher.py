from src.domain.event.product.handler.send_email_when_product_is_created_handler import \
    SendEmailWhenProductIsCreatedHandler
from src.domain.event.shared.dispatcher.event_dispatcher import EventDispatcher


class TestEventDispatcher:

    def test_register_an_event(self):
        # When
        event_dispatcher = EventDispatcher()
        event_handler = SendEmailWhenProductIsCreatedHandler()

        event_dispatcher.register("ProductCreatedEvent", event_handler)

        # Then
        assert len(event_dispatcher.event_handlers) == 1
        assert event_dispatcher.event_handlers["ProductCreatedEvent"] == [event_handler]
