class Customer:
    def __init__(self,
                 customer_id: int,
                 customer_name: str,
                 contact_name: str,
                 address: str,
                 city: str,
                 postal_code: str,
                 country: str):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__contact_name = contact_name
        self.__address = address
        self.__city = city
        self.__postal_code = postal_code
        self.__country = country

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def customer_name(self):
        return self.__customer_name

    @property
    def contact_name(self):
        return self.__contact_name

    @property
    def address(self):
        return self.__address

    @property
    def city(self):
        return self.__city

    @property
    def postal_code(self):
        return self.__postal_code

    @property
    def country(self):
        return self.__country
