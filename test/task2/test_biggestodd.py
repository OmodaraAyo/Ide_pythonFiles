from unittest import TestCase
from selfpractice.practices.bigodd import biggest_odd

class TestBiggestOdd(TestCase):
    def test_biggest_odd(self):
        self.assertEqual(biggest_odd("23783"), 7)

    def test_bigNum(self):
        self.assertEqual(biggest_odd("2938"), 9)

    def test_odd(self):
        self.assertEqual(biggest_odd("312"), 3)
