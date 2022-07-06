from fastapi import APIRouter
from peewee import SqliteDatabase

from src.infrastructure.customer.repository.peewee.customer_model import CustomerModel
from src.infrastructure.customer.repository.peewee.customer_repository import CustomerRepository
from src.infrastructure.shared.repository.peewee.base_model import sqlite_db
from src.usecase.customer.create.create_customer_dto import InputCreateCustomerDTO
from src.usecase.customer.create.create_customer_usecase import CreateCustomerUseCase

router = APIRouter()


class CustomerFactory:
    db_connection: SqliteDatabase = sqlite_db

    @staticmethod
    def __db_instance():
        if CustomerFactory.db_connection.is_closed():
            CustomerFactory.db_connection.connect()
            CustomerFactory.db_connection.create_tables([CustomerModel])
        return CustomerFactory.db_connection

    @staticmethod
    def create_customer_usecase() -> CreateCustomerUseCase:
        CustomerFactory.__db_instance()
        return CreateCustomerUseCase(CustomerRepository())


@router.post("/create")
def create_customer(input_dto: InputCreateCustomerDTO):
    customer_usecase = CustomerFactory.create_customer_usecase()
    return customer_usecase.execute(input_dto)
