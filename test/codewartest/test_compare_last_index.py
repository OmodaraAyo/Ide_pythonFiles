import unittest

from selfpractice.codewar.compare_last_index import *


class TestCompareLastIndex(unittest.TestCase):

    def test_last_index_functionality_1(self):
        actual = last_index("abc", "bc")
        self.assertTrue(actual)

    def test_last_character_funtionality(self):
        actual = last_character("abc")
        self.assertEqual("c", actual)

    def test_last_index_functionality_2(self):
        actual = last_index("samurai", "ai")
        self.assertTrue(actual)

    def test_last_index_functionality_3(self):
        actual = last_index("sumo", "omo")
        self.assertTrue(actual)

    def test_match_last_character(self):
        actual = match_last_character("abc", "bc")
        self.assertTrue(actual)