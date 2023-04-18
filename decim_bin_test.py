import unittest
from decimal_binario import bin2dec
from decimal_binario import dec2bin

class TestConversor(unittest.Testcase):
    def test_bin2dec(self):
        self.assertEqual(bin2dec('111'), 7)
    def test_dec2bin(self):
        self.assertEqual(dec2bin(7), '111')

if __name__ == '__main__':
    unittest.main()
