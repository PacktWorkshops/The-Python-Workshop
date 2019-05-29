import unittest
import hello_world
from sum_to_10 import result
from multiply import list_product

class Lesson3ExamplesUnitTests(unittest.TestCase):

    def test_welcome(self):
        # Simply test we don't hit an exception
        hello_world.welcome()

    def test_docstring(self):
         self.assertEqual(hello_world.__doc__, 'This script prints hello world and not much else!')
    
    def test_today(self):
        # Simply test we can import, which will execute the short script
        import today
    
    def test_sum_to_10(self):
        self.assertEqual(result, 55)
      
    def test_multiply(self):
        self.assertEqual(list_product([-1, 2, 3]), -6)
    

if __name__ == '__main__':
    unittest.main()