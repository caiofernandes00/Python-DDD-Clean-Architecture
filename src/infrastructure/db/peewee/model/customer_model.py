from peewee import CharField, BooleanField, IntegerField

from src.infrastructure.db.peewee.model.base_model import BaseModel


class CustomerModel(BaseModel):
    id = CharField(primary_key=True)
    name = CharField(null=False)
    street = CharField(null=False)
    number = IntegerField(null=False)
    zipcode = CharField(null=False)
    city = CharField(null=False)
    active = BooleanField(default=False)
    reward_points = IntegerField(default=1)

    class Meta:
        db_table = 'customer'
