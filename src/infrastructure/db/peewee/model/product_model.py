from peewee import CharField, FloatField

from src.infrastructure.db.peewee.model.base_model import BaseModel


class ProductModel(BaseModel):
    id = CharField(primary_key=True)
    name = CharField(null=False)
    price = FloatField(null=False)

    class Meta:
        db_table = 'product'
