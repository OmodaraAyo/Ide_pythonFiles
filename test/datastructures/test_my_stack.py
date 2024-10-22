import unittest

from mydatastructures.my_stack import MyStack

class TestMyStack(unittest.TestCase):

    def setUp(self):
        self.stack = MyStack()

    def test_that_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_to_add_an_element_in_the_stack(self):
        self.assertEqual("Apple", self.stack.append("Apple"))

    def test_to_peek_through_the_last_element_in_the_stack(self):
        self.stack.append("Apple")
        self.stack.append("Banana")
        self.assertEqual("Banana", self.stack.peek())

    def test_that_if_peeked_through_an_empty_stack_error_is_thrown(self):
        with self.assertRaises(RuntimeError) as context:
            self.stack.peek()
        self.assertEqual("Stack is empty", str(context.exception))

    def test_to_pop_an_item_from_a_full_stack(self):
        self.stack.append("Apple")
        self.stack.append("Banana")
        self.stack.append("pawpaw")
        self.assertEqual("pawpaw", self.stack.pop())

    def test_that_if_an_element_is_popped_from_an_empty_stack_error_is_thrown(self):
        with self.assertRaises(RuntimeError) as context:
            self.stack.pop()
        self.assertEqual("Stack is empty", str(context.exception))

    def test_to_get_index_of_an_element_in_the_stack(self):
        self.stack.append("Apple")
        self.stack.append("Banana")
        self.stack.append("pawpaw")
        self.assertEqual(1, self.stack.search("Banana"))

    def test_that_searching_through_an_empty_stack_error_is_thrown(self):
        self.assertEqual(-1, self.stack.search("Banana"))