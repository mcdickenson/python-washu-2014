import unittest
import lab1

class TestLab1Code(unittest.TestCase):

	def setUp(self): 
		self.x2 = "10000"
		self.y2 = "10"
		self.y10 = "2"
		self.xplusy = "10010"
		self.xtimesy = "100000"

	# Correctness tests 

	# binarify
	def test_binarify_16(self):
		self.assertEqual(lab1.binarify(16), "10000")

	def test_binarify_127(self):
		self.assertEqual(lab1.binarify(127), "1111111")

	def test_binarify_0(self):
		self.assertEqual(lab1.binarify(0), "0")

	def test_binarify_negative(self):
		self.assertEqual(lab1.binarify(-16), "0")


	# int_to_base
	def test_int_to_base_2(self):
		self.assertEqual(lab1.int_to_base(123, 2), lab1.binarify(123))

	def test_int_to_base_3(self):
		self.assertEqual(lab1.int_to_base(12, 3), "110")

	def test_int_to_base_10(self):
		self.assertEqual(lab1.int_to_base(16, 10), "16")

	def test_int_to_base_0(self):
		self.assertEqual(lab1.int_to_base(16, 0), "0")

	def test_int_to_base_negative(self):
		self.assertEqual(lab1.int_to_base(-16, 2), "-10000")


	# base_to_int
	def test_base_to_int_16(self):
		self.assertEqual(lab1.base_to_int("10000", 2), 16)

	def test_base_to_int_3(self):
		self.assertEqual(lab1.base_to_int("110", 3), 12)

	def test_base_to_int_10(self):
		self.assertEqual(lab1.base_to_int("16", 10), 16)

	def test_base_to_int_0(self):
		self.assertEqual(lab1.base_to_int("123", 0), 0)

	def test_base_to_int_negative(self):
		self.assertEqual(lab1.base_to_int("-10000", 2), -16)


	# flexibase methods
	def test_flexibase_add_base_2(self):
		self.assertEqual(lab1.flexibase_add(self.x2, self.y2, 2, 2), self.xplusy)

	def test_flexibase_add_base_2_10(self):
		self.assertEqual(lab1.flexibase_add(self.x2, self.y10, 2, 10), self.xplusy)

	def test_flexibase_multiply_base_2(self):
		self.assertEqual(lab1.flexibase_multiply(self.x2, self.y2, 2, 2), self.xtimesy)

	def test_flexibase_multiply_base_10(self):
		self.assertEqual(lab1.flexibase_multiply(self.x2, self.y10, 2, 10), self.xtimesy)


	# romanify 
	def test_romanify_3(self):
		self.assertEqual(lab1.romanify(3), "III")

	def test_romanify_9(self):
		self.assertEqual(lab1.romanify(9), "IX")

	def test_romanify_10(self):
		self.assertEqual(lab1.romanify(10), "X")

	def test_romanify_49(self):
		self.assertEqual(lab1.romanify(49), "XLIX")

	def test_romanify_99(self):
		self.assertEqual(lab1.romanify(99), "XCIX")

	def test_romanify_3999(self):
		self.assertEqual(lab1.romanify(3999), "MMMCMXCIX")


if __name__ == '__main__':
  unittest.main()	

