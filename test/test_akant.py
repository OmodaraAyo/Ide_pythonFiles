from unittest import TestCase
from decimal import Decimal
from classes_in_python import Akant


class TestAkant(TestCase):
        def test_that_account_can_deposit(self):
            a1 = Akant("john","0000")
            a1.deposit(10000)
            self.assertEqual(a1.balance, 10000)