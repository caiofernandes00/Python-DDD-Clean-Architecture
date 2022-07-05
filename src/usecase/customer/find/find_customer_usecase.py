from src.domain.customer.repository.customer_repository_interface import CustomerRepositoryInterface
from src.usecase.customer.find.find_customer_dto import InputFindCustomerDTO, OutputFindCustomerDTO, \
    OutputFindCustomerAddressDTO


class FindCustomerUseCase:

    def __init__(self, customer_repository: CustomerRepositoryInterface):
        self.__customer_repository = customer_repository

    def execute(self, input_dto: InputFindCustomerDTO) -> OutputFindCustomerDTO:
        customer = self.__customer_repository.find(input_dto.id)
        return OutputFindCustomerDTO(id=customer.id, name=customer.name,
                                     address=OutputFindCustomerAddressDTO(street=customer.address.street,
                                                                          city=customer.address.city,
                                                                          number=customer.address.number,
                                                                          zip=customer.address.zipcode))
