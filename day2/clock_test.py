import unittest
from clock import Clock

class ClockTest(unittest.TestCase):

  def test_on_the_hour(self):
    self.assertEqual("08:00", Clock.at(8).__str__() )
    self.assertEqual("09:00", Clock.at(9).__str__() )

  def test_past_the_hour(self):
    self.assertEqual("11:09", Clock.at(11, 9).__str__() )

  def test_add_a_few_minutes(self):
    clock = Clock.at(10) + 3
    self.assertEqual("10:03", clock.__str__())

  def test_add_over_an_hour(self):
    clock = Clock.at(10) + 61
    self.assertEqual("11:01", clock.__str__())

  def test_wrap_around_at_midnight(self):
    clock = Clock.at(23, 30) + 60
    self.assertEqual("00:30", clock.__str__())

  def test_subtract_minutes(self):
    clock = Clock.at(10) - 90
    self.assertEqual("08:30", clock.__str__())

  def test_equivalent_clocks(self):
    clock1 = Clock.at(15, 37)
    clock2 = Clock.at(15, 37)
    self.assertEqual(clock1, clock2)

  def test_inequivalent_clocks(self):
    clock1 = Clock.at(15, 37)
    clock2 = Clock.at(15, 36)
    clock3 = Clock.at(14, 37)
    self.assertNotEqual(clock1, clock2)
    self.assertNotEqual(clock1, clock3)

  def test_wrap_around_backwards(self):
    clock = Clock.at(0, 30) - 60
    self.assertEqual("23:30", clock.__str__())

if __name__ == '__main__':
  unittest.main() 

