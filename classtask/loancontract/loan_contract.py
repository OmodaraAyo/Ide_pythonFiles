
class LoanContract():

    def __init__(self, borrower, interest_rate, loan_amount, loan_period):
        self.borrower = borrower
        self._interest_rate = interest_rate
        self.loan_amount = loan_amount
        self.loan_period = loan_period

    @property
    def get_borrower(self):
        return self.borrower

    @property
    def _interest_rate(self):
        return self._rate

    @property
    def loan_amount(self):
        return self._loan_amount

    @property
    def loan_period(self):
        return self.period

    @_interest_rate.setter
    def _interest_rate(self, rate):
        if not isinstance(rate, (int,float)):
            raise TypeError("Interest rate must be a number. eg: 10,20,30...")
        if rate < 1:
            raise ValueError("Interest rate must be greater than or equal to one.")
        self._rate = rate / 100

    @loan_amount.setter
    def loan_amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Loan amount must be a number. eg: 2000,5000,7000...")
        if amount < 1000:
            raise ValueError("minimum loan amount is -> $1000.")
        self._loan_amount = amount

    @loan_period.setter
    def loan_period(self, period):
        if not isinstance(period, (int,float)):
            raise TypeError("Loan period must be a number. eg: 1,2,3...")
        if period < 1:
            raise ValueError("loan period cannot be less than or equal to zero.")
        self.period = period * 12

    def compute_monthly_payment(self):
        principal = self.loan_amount
        monthly_interest_rate = self._interest_rate / 12
        duration_in_months = self.loan_period
        value = (1 + monthly_interest_rate)**duration_in_months
        monthly_payment = (principal * monthly_interest_rate * value) / (value - 1)
        return round(monthly_payment, 2)

    def total_payment(self):
        return round(self.compute_monthly_payment() * self.loan_period, 2)

