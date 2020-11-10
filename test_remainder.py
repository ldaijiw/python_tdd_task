from remainder import Calculations
import unittest

class TestRemainder(unittest.TestCase):
    class_inst = Calculations()

    def test_remainder_zero(self):
        self.assertTrue(self.class_inst.remainder_zero(20, 5))
    
    def test_remainder_nonzero(self):
        self.assertFalse(self.class_inst.remainder_zero(17, 2))

    def test_positive_values(self):
        self.assertTrue(self.class_inst.positive_values(10, 0.5, 0.1, 0.0001))
    
    def test_negative_values(self):
        self.assertFalse(self.class_inst.positive_values(0, -1, -2))