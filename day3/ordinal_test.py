import unittest
import ordinal

class OrdinalTest(unittest.TestCase):

  def setup(self):
    pass 

  def test_zero(self):
    self.assertEqual("0th", ordinal.ordinal(0))

  def test_first(self):
    self.assertEqual("1st", ordinal.ordinal(1))

  def test_second(self):
    self.assertEqual("2nd", ordinal.ordinal(2))

  def test_third(self):
    self.assertEqual("3rd", ordinal.ordinal(3))

  def test_fourth(self):
    self.assertEqual("4th", ordinal.ordinal(4))

  def test_eleventh(self):
    self.assertEqual("11th", ordinal.ordinal(11))

  def test_twelfth(self):
    self.assertEqual("12th", ordinal.ordinal(12))

  def test_one_thousand_two(self):
    self.assertEqual("1002nd", ordinal.ordinal(1002))

  def test_negative_one(self):
    self.assertEqual("-1st", ordinal.ordinal(-1))

  def test_decimal(self):
    self.assertEqual("1st", ordinal.ordinal(1.0))

  def test_string_input(self):
    self.assertEqual("1st", ordinal.ordinal("1"))
    self.assertEqual("Improper input", ordinal.ordinal("abc"))

if __name__ == '__main__':
  unittest.main()