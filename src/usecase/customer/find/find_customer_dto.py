from dataclasses import dataclass


@dataclass
class InputFindCustomerDTO:
    id: str


@dataclass
class OutputFindCustomerAddressDTO:
    street: str
    city: str
    number: int
    zip: str


@dataclass
class OutputFindCustomerDTO:
    id: str
    name: str
    address: OutputFindCustomerAddressDTO
