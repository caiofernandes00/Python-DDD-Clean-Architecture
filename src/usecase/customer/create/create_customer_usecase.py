import uuid

from src.domain.customer.entity.customer import Customer
from src.domain.customer.repository.customer_repository_interface import CustomerRepositoryInterface
from src.domain.customer.value_object.address import Address
from src.usecase.customer.create.create_customer_dto import InputCreateCustomerDTO, OutputCreateCustomerDTO


class CreateCustomerUseCase:

    def __init__(self, customer_repository: CustomerRepositoryInterface):
        self.__customer_repository = customer_repository

    def execute(self, input_dto: InputCreateCustomerDTO) -> OutputCreateCustomerDTO:
        customer_id = str(uuid.uuid4())
        customer = Customer(uid=customer_id, name=input_dto.name)
        customer.change_address(
            Address(street=input_dto.address.street, number=input_dto.address.number, zipcode=input_dto.address.zip,
                    city=input_dto.address.city))
        self.__customer_repository.create(customer)
        return OutputCreateCustomerDTO(id=customer_id, name=input_dto.name, address=input_dto.address)
