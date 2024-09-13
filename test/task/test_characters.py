import unittest
from selfpractice import characters

class TestCharacters(unittest.TestCase):
    def test_To_Count_Characters(self):
        actual = {"A": 1, "Y": 1, "O": 1, "D": 1, "E": 2, "L": 1}
        expected = characters.dict_characters("AYODELE")
        self.assertEqual(actual,expected)

    def test_To_Count_CharactersSmallLetters(self):
        actual = {"A": 1, "Y": 1, "O": 1, "D": 1, "E": 2, "L": 1}
        expected = characters.dict_characters("ayodele")
        self.assertEqual(actual,expected)

    def test_To_Count_Characters_Both_SmallLetters_And_CapitalLetter(self):
        actual ={"A": 1, "Y": 1, "O": 1, "D": 1, "E": 2, "L": 1}
        expected = characters.dict_characters("AyOdEle")
        self.assertEqual(actual,expected)

