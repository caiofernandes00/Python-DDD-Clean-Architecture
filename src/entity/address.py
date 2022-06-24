class Address:
    def __init__(self, street: str, number: int = 0, zipcode: str = "", city: str = ""):
        self.__street = street
        self.__number = number
        self.__zipcode = zipcode
        self.__city = city
        self.validate()

    def validate(self):
        if self.__street.__len__() == 0:
            raise Exception("Street is required")
        if self.__number == 0:
            raise Exception("Number is required")
        if self.__zipcode.__len__() == 0:
            raise Exception("Zip is required")
        if self.__city.__len__() == 0:
            raise Exception("City is required")

    def __str__(self):
        return f"{self.__street}, {self.__number}, {self.__zipcode} {self.__city}"
