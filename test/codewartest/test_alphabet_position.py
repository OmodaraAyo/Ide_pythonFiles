import unittest

from selfpractice.codewar.alphabet_position import alphabet_position


class TestAlphabetPosition(unittest.TestCase):

    def test_alphabet_position_functionality(self):
        word_input = "The sunset sets at twelve o' clock."
        expected = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
        self.assertEqual(expected, alphabet_position(word_input))

    def test_alphabet_position_functionality_2(self):
        word = "The narwhal bacons at midnight."
        expected = "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
        self.assertEqual(expected, alphabet_position(word))