import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise03
        self.exercises = Exercise03

    def test(self):
        self.assertEqual(self.exercises.my_module.__doc__, 'This script computes the sum of the factorial of a list of numbers')
        
if __name__ == '__main__':
    unittest.main()
