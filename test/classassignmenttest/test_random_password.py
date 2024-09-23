import unittest

from classtask.classassignment.random_password import generate_password

class TestRandomPassword(unittest.TestCase):
    def test_that_generatePassword_function_exist(self):
        self.assertTrue(callable(generate_password))

    def test_that_password_generator_has_length_of_8_characters_length(self):
        actual = generate_password(8)
        self.assertEqual(len(actual), 8)

    def test_that_given_length_lessThan_8_password_generator_returnsInvalidLength(self):
        actual = generate_password(7)
        expected = "password length must be between 8 and 16 characters"
        self.assertEqual(expected, actual)
    def test_that_given_a_string_parameter_password_generator_returns_A_Number_isRequired(self):
        actual = generate_password("<PASSWORD>")
        expected = "A length of password must be an integer"
        self.assertEqual(expected, actual)

