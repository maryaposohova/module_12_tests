import unittest
import calk_11


class NewCalkTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calk_11.sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(calk_11.pow(3,3), 27)




