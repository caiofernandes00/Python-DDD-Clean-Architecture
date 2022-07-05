from src.domain.event.product.product_created_event import ProductCreatedEvent
from src.domain.event.shared.event_handler_interface import EventHandlerInterface


class SendEmailWhenProductIsCreatedHandler(EventHandlerInterface):

    def handle(self, event: ProductCreatedEvent) -> ProductCreatedEvent:
        print("Sending email...")
        return event
