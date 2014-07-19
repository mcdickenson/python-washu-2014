import unittest
import polymorphism

class TestInClassCode(unittest.TestCase):
  
  def setUp(self):
    return
  
  def test_dog(self):
    dog = polymorphism.Dog("Fido")
    
    self.assertEqual(dog.talk(), "Woof! Woof!")
    self.assertEqual(dog.bark(), "Woof! Woof!")
    
    
if __name__ == '__main__':
  unittest.main()