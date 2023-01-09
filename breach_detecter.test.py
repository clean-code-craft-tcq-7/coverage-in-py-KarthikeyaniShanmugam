import unittest
from breach_detecter import *
class BreachDetectorTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(infer_breach(2, 3, 5) == 'TOO_LOW')
    self.assertTrue(infer_breach(4, 1, 10) == 'NORMAL')
    self.assertTrue(infer_breach(-4, -100, -2) == 'NORMAL')
    self.assertTrue(infer_breach(0.4, 0.1, 1.0) == 'NORMAL')
    self.assertTrue(infer_breach(1.2, 0.1, 1.0) == 'TOO_HIGH')
    self.assertTrue(infer_breach(0.02, 0.1, 1.0) == 'TOO_LOW')

if __name__ == '__main__':
  unittest.main()