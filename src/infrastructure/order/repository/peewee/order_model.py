from peewee import CharField, FloatField, ForeignKeyField

from src.infrastructure.shared.repository.peewee.base_model import BaseModel
from src.infrastructure.customer.repository.peewee.customer_model import CustomerModel


class OrderModel(BaseModel):
    id = CharField(primary_key=True)
    customer = ForeignKeyField(CustomerModel, field='id', backref="customer", db_column="customer_id")
    total = FloatField(null=False)

    customer_id: str

    class Meta:
        db_table = 'order'
