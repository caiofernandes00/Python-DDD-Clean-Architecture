class Address:
    def __init__(self, street: str, number: int = 0, zipcode: str = "", city: str = ""):
        self.__street = street
        self.__number = number
        self.__zipcode = zipcode
        self.__city = city
        self.validate()

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number

    @property
    def zipcode(self):
        return self.__zipcode

    @property
    def city(self):
        return self.__city

    def validate(self):
        self.__validate_street()
        self.__validate_number()
        self.__validate_zipcode()
        self.__validate_city()

    def __validate_street(self):
        if self.__street.__len__() == 0:
            raise Exception("Street is required")

    def __validate_number(self):
        if self.__number == 0:
            raise Exception("Number is required")
        elif self.__number < 0:
            raise Exception("Number should not be negative")

    def __validate_zipcode(self):
        if self.__zipcode.__len__() == 0:
            raise Exception("Zip is required")

    def __validate_city(self):
        if self.__city.__len__() == 0:
            raise Exception("City is required")

    def __str__(self):
        return f"{self.__street}, {self.__number}, {self.__zipcode} {self.__city}"
