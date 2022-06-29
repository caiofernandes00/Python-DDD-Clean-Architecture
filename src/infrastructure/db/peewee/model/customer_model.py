from peewee import CharField, BooleanField, IntegerField

from src.infrastructure.db.peewee.model.base_model import BaseModel


class Customer(BaseModel):
    id = CharField(unique=True, null=False, index=True)
    name = CharField(null=False)
    street = CharField(null=False)
    number = IntegerField(null=False)
    zipcode = CharField(null=False)
    city = CharField(null=False)
    activate = BooleanField(default=False)
    reward_points = IntegerField(default=1)
