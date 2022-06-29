from peewee import CharField, FloatField, ForeignKeyField

from src.infrastructure.db.peewee.model.base_model import BaseModel
from src.infrastructure.db.peewee.model.customer_model import Customer


class Order(BaseModel):
    id = CharField(unique=True, null=False, index=True)
    customer_id = ForeignKeyField(Customer, field='id', backref="customer")
    total = FloatField(null=False)
