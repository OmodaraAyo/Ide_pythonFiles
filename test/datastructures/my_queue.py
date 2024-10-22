import unittest

from mydatastructures.my_queue import MyQueue


class TestMYQueue(unittest.TestCase):

    def setUp(self):
        self.queue = MyQueue()

    def test_to_add_element_in_the_queue(self):
        self.assertTrue(self.queue.add("Terry"))

    def test_to_retrieve_the_element_at_the_head_of_the_queue(self):
        self.assertTrue(self.queue.add("Terry"))
        self.assertTrue(self.queue.add("Mary"))
        self.assertTrue(self.queue.add("Fox"))
        self.assertEqual("Terry", self.queue.element())

    def test_to_insert_a_specific_element_into_the_queue(self):
        self.assertTrue(self.queue.offer("Terry"))

    def test_to_retrieve_the_element_at_the_head_of_the_queue_with_another_method(self):
        self.assertTrue(self.queue.offer("Jane"))
        self.assertTrue(self.queue.offer("Fox"))
        self.assertEqual("Jane",self.queue.peek())

    def test_to_peek_an_element_when_queue_is_empty(self):
        self.assertEqual(None, self.queue.peek())

    def test_to_remove_the_head_of_the_queue(self):
        self.assertTrue(self.queue.offer("John"))
        self.assertTrue(self.queue.offer("Fox"))
        self.assertTrue(self.queue.offer("Jane"))
        self.assertEqual("John",self.queue.poll())
        self.assertEqual("Fox", self.queue.poll())
        self.assertEqual("Jane", self.queue.poll())


    def test_to_remove_the_head_of_the_queue_with_a_different_method(self):
        self.assertTrue(self.queue.offer("Mikel"))
        self.assertEqual("Mikel", self.queue.remove())