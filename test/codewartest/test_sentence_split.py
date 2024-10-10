import unittest

from selfpractice.codewar.sentence_split import *
class TestSentenceSplit(unittest.TestCase):

    def test_reverse_sentence_functionality_B(self):
        my_input = "Welcome"
        expected = "emocleW"
        actual = reverse_sentence(my_input)
        self.assertEqual(expected, actual)

    def test_sentence_split_functionality_A(self):
        my_input = "The boy is very intellegent and brave"
        expected = "The boy is very tnegelletni and evarb"
        actual = split_sentence(my_input)
        self.assertEqual(expected, actual)
