from peewee import CharField, FloatField

from src.infrastructure.shared.repository.peewee.base_model import BaseModel


class ProductModel(BaseModel):
    id = CharField(primary_key=True)
    name = CharField(null=False)
    price = FloatField(null=False)

    class Meta:
        table_name = 'product'
