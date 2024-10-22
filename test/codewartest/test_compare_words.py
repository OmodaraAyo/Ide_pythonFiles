import unittest

from selfpractice.codewar.compare_words import solution

class TestCompareWords(unittest.TestCase):

    def test_compare_words_functionality(self):
        self.assertTrue(solution("samurai", "ai"))

    def test_compare_words_functionality2(self):
        self.assertFalse(solution("sumo", "omo"))

    def test_compare_words_functionality3(self):
        self.assertTrue("sensei", "i")

    def test_compare_words_functionality4(self):
        self.assertFalse(solution("abc", "abcd"))

    def test_compare_words_functionality5(self):
        self.assertTrue("abcabc", "bc")
