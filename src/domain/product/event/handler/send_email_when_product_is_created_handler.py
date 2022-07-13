from src.domain.product.event.product_created_event import ProductCreatedEvent
from src.domain.shared.event.event_handler_interface import EventHandlerInterface


class SendEmailWhenProductIsCreatedHandler(EventHandlerInterface):

    def handle(self, event: ProductCreatedEvent) -> None:
        print("Sending email...")
