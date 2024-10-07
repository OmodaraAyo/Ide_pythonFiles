import random


class Account:
    def __init__(self, name, phone):
        self._name = name
        self.__phone = phone
        self.__balance = 0.00
        self.account_number = self.__generate_account_number()

    @property
    def __phone(self):
        return self._phone

    @__phone.setter
    def __phone(self, phone_number):
        if len(phone_number) != 11:
            raise ValueError("Invalid phone number")
        self._phone = phone_number

    def __generate_account_number(self):
        return "222" + str(random.randrange(10000000, 999999999))

    def __str__(self):
        return f"""
        Name: {self._name}
        Phone: {self.__phone}
        Balance: {self.__balance}
        Account Number: {self.account_number}"""


a1 = Account(name="John", phone="08034734618")
print(a1)