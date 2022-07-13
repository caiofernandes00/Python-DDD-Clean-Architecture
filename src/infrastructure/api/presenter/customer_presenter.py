from dict2xml import dict2xml

from src.usecase.customer.create.create_customer_dto import OutputCreateCustomerDTO


class CustomerPresenter:

    @staticmethod
    def to_xml(data: OutputCreateCustomerDTO):
        dict2xml(data, pretty=True)
