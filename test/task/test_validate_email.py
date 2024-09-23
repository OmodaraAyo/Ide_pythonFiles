import unittest
from classtask.task1.validate_emails import validate_email

class Test_validate_email(unittest.TestCase):
    def test_that_validate_email_exist(self):
        validate_email("ayodeleomod@gmail.com")
    def test_that_validate_email_functionality(self):
        email = "ayodeleomodara@gmail.com"
        actual = validate_email(email)
        self.assertTrue(actual)

    def test_that_validate_email_is_invalid(self):
        email = "ayodeleomodaragmail.com"
        actual = validate_email(email)
        self.assertFalse(actual)

    def test_that_validate_email_with_underscore_is_invalid(self):
        email = "ayodeleom_odara@gmail.com"
        actual = validate_email(email)
        self.assertFalse(actual)

    def test_that_validate_email_with_space_is_invalid(self):
        email = "ayode leomodara@gmail.com"
        actual = validate_email(email)
        self.assertFalse(actual)

    def test_that_validate_email_with_double_At_is_invalid(self):
        email = "ayode@leomodara@gmail.com"
        actual = validate_email(email)
        self.assertFalse(actual)
