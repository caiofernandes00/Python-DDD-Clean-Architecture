from peewee import CharField, FloatField

from src.infrastructure.db.peewee.model.base_model import BaseModel


class Product(BaseModel):
    id = CharField(unique=True, null=False, index=True)
    name = CharField(null=False)
    price = FloatField(null=False)
