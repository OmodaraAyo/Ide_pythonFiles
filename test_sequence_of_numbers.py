import unittest
from classtask.task1.sequence_Of_Numbers import list_of

class TestSequence_Of_Numbers(unittest.TestCase):
    def test_that_list_of_exist(self):
        list_of("1")

    def test_list_of_Functionality(self):
        number = "34,67,55,33,12,98"
        actual = list_of(number)
        expected = f"['34', '67', '55', '33', '12', '98'],('34', '67', '55', '33', '12', '98')"
        self.assertEqual(expected, actual)