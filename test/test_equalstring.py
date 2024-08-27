from unittest import TestCase
from selfpractice.equalstring import equal_strings

class TestEqualString(TestCase):
    def test_equalstring(self):
        self.assertEqual(equal_strings("love", "evol"), True)

    def test_equalstring2(self):
        self.assertEqual(equal_strings("age", "bread"), False)

    def test_equalstring3(self):
        self.assertEqual(equal_strings("daddy", "mammy"), False)

    def test_equalstring4(self):
        self.assertEqual(equal_strings("Hippopotamus", "Hippopotemus"), False)
