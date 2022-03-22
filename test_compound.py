import unittest
from Compound import CompoundCalc 

class TestCompound(unittest.TestCase):

    def setUp(self):
       self.compound = CompoundCalc()

    def test_calc_compound(self):
        self.assertEqual(self.compound.calc_compound(5000, 5, 12, 10), 8235.0474884514)

    def test_cagr(self):
        self.assertEqual(self.compound.cagr(176000, 64900, 3),  39.45132882872278)
  


if __name__ == '__main__':
    unittest.main()