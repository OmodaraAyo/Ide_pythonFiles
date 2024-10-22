import unittest

from selfpractice.codewar.digits_squared import square_digits

class TestDigitSquared(unittest.TestCase):

    def test_digit_squared_functionality(self):
        self.assertEqual(0,square_digits(0))

    def test_digit_squared_functionality_ii(self):
        self.assertEqual(811181,square_digits(9119))

    def test_digit_squared_functionality_iii(self):
        self.assertEqual(36493649,square_digits(6767))