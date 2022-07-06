import dataclasses

from fastapi.testclient import TestClient

from src.infrastructure.api.server import app
from src.usecase.customer.create.create_customer_dto import InputCreateCustomerDTO, InputCreateCustomerAddressDTO


class TestE2ECustomer:
    client = TestClient(app)

    def test_create_customer(self):
        input_dto = InputCreateCustomerDTO(name="name",
                                           address=InputCreateCustomerAddressDTO(street="St Wall", number=1,
                                                                                 zip="12343-555", city="OP"))
        response = self.client.post("/customer/create", json=dataclasses.asdict(input_dto))
        assert response.status_code == 200
