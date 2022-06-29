from peewee import CharField, FloatField, ForeignKeyField, IntegerField

from src.infrastructure.db.peewee.model.base_model import BaseModel
from src.infrastructure.db.peewee.model.order_model import Order
from src.infrastructure.db.peewee.model.product_model import Product


class OrderItem(BaseModel):
    id = CharField(unique=True, null=False, index=True)
    order_id = ForeignKeyField(Order, field='id', backref="order")
    product_id = ForeignKeyField(Product, field='id', backref="product")
    quantity = IntegerField(null=False)
    name = CharField(null=False)
    price = FloatField(null=False)
