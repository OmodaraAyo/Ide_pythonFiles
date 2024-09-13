import unittest
from classtask.charactersswap import swapchars2

class TestSwappingChars(unittest.TestCase):
    def test_that_swappingchars_exist(self):
        swapchars2("ayo", "del")
    def test_swappingchars_functionality(self):
        actual = swapchars2("abc", "xyz")
        expected = "xyc abz"
        self.assertEqual(expected, actual)
    def test_swapchars_functionality2(self):
        actual = swapchars2("ayo", "del")
        expected = "del ayz"