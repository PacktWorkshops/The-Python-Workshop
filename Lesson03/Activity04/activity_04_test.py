import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Activity04
        self.exercises = Activity04

    def test(self):
        self.assertEqual(self.exercises.fibonacci_recursive(10), 55)
        
if __name__ == '__main__':
    unittest.main()
