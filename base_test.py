import unittest
from base import *

class TestBaseChanger(unittest.TestCase):
#10 to 2/8/16
    def test_102(self):
        res = dec_bin(10)
        self.assertEqual(res, "1010")
        
    def test_108(self):
        res = dec_oct(10)
        self.assertEqual(res, "12")

    def test_1016(self):
        res = dec_hex(10)
        self.assertEqual(res, "A")
#2 to 8/10/16
    '''def test_28(self):
        res = bin_oct(1010)
        self.assertEqual(res, "12")'''
        
    def test_210(self):
        res = bin_dec(1010)
        self.assertEqual(res, "10")
    '''
    def test_216(self):
        res = bin_hex(1010)
        self.assertEqual(res, "A")'''
#8 to 2/10/16
    def test_82(self):
        res = oct_bin(12)
        self.assertEqual(res, "1010")

    def test_810(self):
        res = oct_dec(12)
        self.assertEqual(res, "10")

    def test_816(self):
        res = oct_hex(12)
        self.assertEqual(res, "A")
#16 to 2/8/10
    def test_162(self):
        res = hex_bin("A")
        self.assertEqual(res, "1010")

    def test_168(self):
        res = hex_oct("A")
        self.assertEqual(res, "12")

    def test_1610(self):
        res = hex_dec("A")
        self.assertEqual(res, "10")

if __name__ == '__main__':
    unittest.main()
