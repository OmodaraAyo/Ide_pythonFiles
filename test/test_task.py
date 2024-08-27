import unittest
from selfpractice.task import dict_cube

class TestTask(unittest.TestCase):
    def testTask(self):
        self.assertEqual(dict_cube([1,2,3,4,5]),{1:1,2:8,3:27,4:64,5:125})