import unittest
from src.calculator import add, subtract, divide 

class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(-1, -1), -2)
  def test_subtract(self):
    self.assertEqual(subtract(5, 2), 3)
    self.assertEqual(subtract(-3, 1), -4)
    self.assertEqual(subtract(-2, -1), -1)
  def test_divide(self):
    self.assertEqual(divide(8, 2), 4)
    self.assertEqual(divide(0, 6), 0)
    self.assertEqual(divide(-4, 2), -2)

if __name__ == '__main__':
   unittest.main()