import unittest

from selfpractice.codewar.pascal_cases import passPascalOf


class TestPascalCases(unittest.TestCase):
    def test_that_passPascalOf_function_exist(self):
        passPascalOf("Ayodele")

    def test_that_passPascalOf_functionality(self):
        actual = passPascalOf("the_stealth_warrior")
        expected = "theStealthWarrior"
        self.assertEqual(actual, expected)