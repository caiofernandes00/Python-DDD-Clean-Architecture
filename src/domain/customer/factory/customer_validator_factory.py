from src.domain.customer.validator.customer_vanilla_validator import CustomerVanillaValidator
from src.domain.shared.validator.validator_interface import ValidatorInterface


class CustomerValidatorFactory:
    def __init__(self):
        pass

    @staticmethod
    def create() -> ValidatorInterface:
        return CustomerVanillaValidator()
