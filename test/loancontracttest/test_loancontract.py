import unittest

from classtask.loancontract.loan_contract import LoanContract

class TestLoanContract(unittest.TestCase):
    def setUp(self):
        self.mikel_loan = LoanContract("Bamdele Mikel", 20, 5000, 2)
        self.jerry_loan = LoanContract("Jerry watkins", 40.0, 5000.00, 3.00)

    def test_that_each_loan_contract_must_have_a_name(self):
        self.assertEqual("Bamdele Mikel", self.mikel_loan.borrower)

    def test_that_each_loan_contract_must_have_interest_rate(self):
        self.assertEqual(0.20, self.mikel_loan._interest_rate)

    def test_that_each_loan_contract_must_have_a_loan_amount(self):
        self.assertEqual(5000, self.mikel_loan.loan_amount)

    def test_that_each_loan_contract_must_have_a_loan_period(self):
        self.assertEqual(24, self.mikel_loan.loan_period)

    def test_that_interest_rate_input_is_valid_if_a_float_number_is_given(self):
        self.assertEqual(0.40, self.jerry_loan._interest_rate)

    def test_that_loan_amount_input_is_valid_if_a_float_number_is_given(self):
        self.assertEqual(5000, self.jerry_loan.loan_amount)

    def test_that_loan_period_input_is_valid_if_a_float_number_is_given(self):
        self.assertEqual(36, self.jerry_loan.loan_period)

    def test_that_interest_rate_raiseValue_error_if_a_string_is_given(self):
        with self.assertRaises(TypeError) as description:
            self.will_loan = LoanContract("Will loan", "20.0", 5000, 2.00)
        self.assertEqual(str(description.exception), "Interest rate must be a number. eg: 10,20,30...")

    def test_that_loan_amount_raiseValue_error_if_a_string_is_given(self):
        with self.assertRaises(TypeError) as description:
            self.will_loan = LoanContract("Will loan", 20, "5000", 2.00)
        self.assertEqual(str(description.exception), "Loan amount must be a number. eg: 2000,5000,7000...")

    def test_that_loan_period_raiseValue_error_if_a_string_is_given(self):
        with self.assertRaises(TypeError) as description:
            self.will_loan = LoanContract("Will loan", 20, 5000, "2.00")
        self.assertEqual(str(description.exception), "Loan period must be a number. eg: 1,2,3...")

    def test_to_calculate_monthly_payment_on_loan_contract(self):
        self.assertEqual(254.48, self.mikel_loan.compute_monthly_payment())
        self.assertEqual(240.55, self.jerry_loan.compute_monthly_payment())

    def test_to_calculate_total_payment_on_loan_contract(self):
        self.assertEqual(6107.52, self.mikel_loan.total_payment())
        self.assertEqual(8659.80, self.jerry_loan.total_payment())

    def test_to_raise_value_error_if_interest_rate_is_less_than_one(self):
        with self.assertRaises(ValueError) as description:
            self.mark_loan = LoanContract("Mark berry", 0, 5000, 2.00)
        self.assertEqual(str(description.exception), "Interest rate must be greater than or equal to one.")

    def test_to_raise_value_error_if_loan_amount_is_less_than_a_thousand(self):
        with self.assertRaises(ValueError) as description:
            self.mark_loan = LoanContract("Mark berry", 1, 900, 2.00)
        self.assertEqual(str(description.exception), "minimum loan amount is -> $1000.")

    def test_to_raise_value_error_if_loan_period_is_less_than_a_one(self):
        with self.assertRaises(ValueError) as description:
            self.mark_loan = LoanContract("Mark berry", 1, 1000, 0)
        self.assertEqual(str(description.exception), "loan period cannot be less than or equal to zero.")