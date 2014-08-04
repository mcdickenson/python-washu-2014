import unittest
import words

class TestWordsCode(unittest.TestCase):

  def test_has_no_e(self):
    self.assertEqual(words.has_no_e("bet"), False)
    self.assertEqual(words.has_no_e("bit"), True)

  def test_uses_only(self):
    self.assertEqual(words.uses_only("ababab", "a"), False)
    self.assertEqual(words.uses_only("ababab", "ab"), True)

  def test_uses_all(self):
    self.assertEqual(words.uses_all("ababab", "abc"), False)
    self.assertEqual(words.uses_all("ababab", "ab"), True)

  def test_is_abecedarian(self):
    self.assertEqual(words.is_abecedarian("abcxyz"), True)
    self.assertEqual(words.is_abecedarian("abczyx"), False)
