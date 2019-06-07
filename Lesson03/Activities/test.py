import unittest
import import_ipynb
import datetime

class TestLesson03(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Activities
        self.activities = Activities
        print(1)

    def test_format_customer(self):
        self.assertEqual(self.activities.format_customer('Mareike', 'Schmidt'), 'Mareike Schmidt')
        self.assertEqual(self.activities.format_customer('John', 'Smith', location='California'), 'John Smith (California)')
    
    def test_fibonacci_iterative(self):
        self.assertEqual(self.activities.fibonacci_iterative(10), 55)
        self.assertEqual(self.activities.fibonacci_iterative(3), 2)
    
    def test_fibonacci_dynamic(self):
        self.assertEqual(self.activities.fibonacci_dynamic(100), 354224848179261915075)
          
if __name__ == '__main__':
    unittest.main()