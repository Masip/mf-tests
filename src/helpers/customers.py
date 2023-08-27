from src.helpers.customer import Customer


class Customers:
    def __init__(self):
        self.__customers = []

    def add_customer(self, customer: Customer):
        self.__customers.append(customer)

    @property
    def customers(self):
        return self.__customers
