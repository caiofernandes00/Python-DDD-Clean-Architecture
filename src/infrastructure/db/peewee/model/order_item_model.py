from peewee import CharField, FloatField, ForeignKeyField, IntegerField

from src.infrastructure.db.peewee.model.base_model import BaseModel
from src.infrastructure.db.peewee.model.order_model import OrderModel
from src.infrastructure.db.peewee.model.product_model import ProductModel


class OrderItemModel(BaseModel):
    id = CharField(primary_key=True)
    order = ForeignKeyField(OrderModel, field='id', backref="order", db_column="order_id")
    product = ForeignKeyField(ProductModel, field='id', backref="product", db_column="product_id")
    quantity = IntegerField(null=False)
    name = CharField(null=False)
    price = FloatField(null=False)

    order_id: str
    product_id: str

    class Meta:
        db_table = 'order_item'
