from fastapi import APIRouter

from src.infrastructure.api.factory.customer_api_factory import CustomerApiFactory
from src.usecase.customer.create.create_customer_dto import InputCreateCustomerDTO

router = APIRouter()


@router.post("/create")
def create_customer(input_dto: InputCreateCustomerDTO):
    customer_usecase = CustomerApiFactory.create_customer_usecase()
    return customer_usecase.execute(input_dto)
