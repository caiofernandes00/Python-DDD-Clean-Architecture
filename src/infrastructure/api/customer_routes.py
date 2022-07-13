from fastapi import APIRouter
from fastapi.responses import Response

from src.infrastructure.api.factory.customer_api_factory import CustomerApiFactory
from src.infrastructure.api.presenter.customer_presenter import CustomerPresenter
from src.usecase.customer.create.create_customer_dto import InputCreateCustomerDTO

router = APIRouter()


@router.post("/create")
def create_customer(input_dto: InputCreateCustomerDTO):
    customer_usecase = CustomerApiFactory.create_customer_usecase()
    response = customer_usecase.execute(input_dto)

    return Response(content=CustomerPresenter.to_xml(response), media_type="application/xml")
