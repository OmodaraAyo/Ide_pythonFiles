from decimal import Decimal
class Akant:
        #constructor
        def __init__(self, name, pin, balance = 0.00):
                self.name = name.upper()
                self.pin = pin
                self.balance = balance
        def deposit(self, amount):
            if amount < Decimal(0.0):
                    raise ValueError(f'Amount cannot be less than zero')
            self.balance +=  amount
