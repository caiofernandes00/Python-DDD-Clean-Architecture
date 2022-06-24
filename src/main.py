from src.entity.OrderItem import OrderItem
from src.entity.address import Address
from src.entity.customer import Customer
from src.entity.order import Order

if __name__ == "__main__":
    customer = Customer("123", "Wall Street")
    address = Address("St. Vem Diesel", 2, "12345-342", "Mamaco City")
    customer.change_address(address)
    customer.activate()

    item1 = OrderItem("1", "Item 1", 10)
    item2 = OrderItem("2", "Item 2", 20)
    order = Order("1", "123", [item1, item2])
