from unittest import TestCase
from selfpractice.big_odd import biggest_odd

class TestBiggestOdd(TestCase):
    def test_biggest_odd(self):
        self.assertEqual(biggest_odd("23763"), 7)
