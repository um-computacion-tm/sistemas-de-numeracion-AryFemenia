import unittest
from base import *

class TestBaseChanger(unittest.TestCase):
    def test_102(self):
        res = dec_bin(10)
        self.assertEqual(res, "1010")
        
    def test_108(self):
        res = dec_oct(10)
        self.assertEqual(res, "12")

    def test_1016(self):
        res = dec_hex(10)
        self.assertEqual(res, "A")

if __name__ == '__main__':
    unittest.main()
