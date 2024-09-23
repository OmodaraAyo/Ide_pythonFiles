import unittest
from classtask.task2.cees import *
from classtask.task2.capitals import caps_to_small
from classtask.task2.alphabetcounter import alphacount
from classtask.task2.charactersswap import swapchars2


class TestSees(unittest.TestCase):
    def test_that_sees_exist(self):
        sees("ayo")
    def test_sees_functionality(self):
        actual = sees("helloo")
        excpected = "helceloo"
        self.assertEqual(excpected, actual)
    def test_sees_funtionality(self):
        actual = sees("joy")
        excpected = "joyce"
        self.assertEqual(excpected, actual)
    def test_that_caps_to_smalls_exist(self):
        caps_to_small("Ayo")
    def test_caps_to_smalls_functionality(self):
        actual = caps_to_small("AyoDele")
        excpected = "ADyoele"
        self.assertEqual(excpected, actual)
    def test_that_alphabet_counter(self):
        alphacount("Ayodele", "e")

    def test_alphabet_counter_functionality(self):
        actual = alphacount("Ayodele", "e")
        expected = 2
        self.assertEqual(expected, actual)
    def test_alphabet_counter_funtionality_again(self):
        actual = alphacount("Hippopotamus is mad and ppppppp", "p")
        expected = 10
        self.assertEqual(expected, actual)

    def test_swapcharss_functionality(self):
        actual = swapchars2("abc", "xyz")
        excpected = "xyc abz"
        self.assertEqual(excpected, actual)