from peewee import SqliteDatabase

from src.infrastructure.customer.repository.peewee.customer_model import CustomerModel
from src.infrastructure.customer.repository.peewee.customer_repository import CustomerRepository
from src.infrastructure.shared.repository.peewee.base_model import sqlite_db
from src.usecase.customer.create.create_customer_usecase import CreateCustomerUseCase


class CustomerApiFactory:
    db_connection: SqliteDatabase = sqlite_db

    @staticmethod
    def __db_instance():
        if CustomerApiFactory.db_connection.is_closed():
            CustomerApiFactory.db_connection.connect()
            CustomerApiFactory.db_connection.create_tables([CustomerModel])
        return CustomerApiFactory.db_connection

    @staticmethod
    def create_customer_usecase() -> CreateCustomerUseCase:
        CustomerApiFactory.__db_instance()
        return CreateCustomerUseCase(CustomerRepository())
