from peewee import CharField, FloatField, ForeignKeyField, IntegerField

from src.infrastructure.shared.repository.peewee.base_model import BaseModel
from src.infrastructure.order.repository.peewee.order_model import OrderModel
from src.infrastructure.product.repository.peewee.product_model import ProductModel


class OrderItemModel(BaseModel):
    id = CharField(primary_key=True)
    order = ForeignKeyField(OrderModel, field='id', backref="order", column_name="order_id")
    product = ForeignKeyField(ProductModel, field='id', backref="product", column_name="product_id")
    quantity = IntegerField(null=False)
    name = CharField(null=False)
    price = FloatField(null=False)

    order_id: str
    product_id: str

    class Meta:
        table_name = 'order_item'
