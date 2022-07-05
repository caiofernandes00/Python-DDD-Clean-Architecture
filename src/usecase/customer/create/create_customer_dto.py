from dataclasses import dataclass


@dataclass
class InputCreateCustomerAddressDTO:
    street: str
    number: int
    zip: str
    city: str


@dataclass
class InputCreateCustomerDTO:
    name: str
    address: InputCreateCustomerAddressDTO


@dataclass
class OutputCreateCustomerDTO:
    id: str
    name: str
    address: InputCreateCustomerAddressDTO
