import unittest

from classtask.evenoddcounter import eaocounter


class TestEvenOddCounter(unittest.TestCase):
    def test_that_eaocounter_exist(self):
        eaocounter([1,2,3])

    def test_eaocounter_functionality(self):
        actual = eaocounter([2,1,5,7,8])
        expected = [2,3]
        self.assertEqual(expected, actual)
    def test_eaocounter_functionality2(self):
        actual = eaocounter([4,1,5,7,9])
        expected = [1,4]
        self.assertEqual(expected, actual)