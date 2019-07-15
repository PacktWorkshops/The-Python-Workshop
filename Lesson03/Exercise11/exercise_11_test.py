import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise11
        self.exercises = Exercise11

    def test(self):
        self.assertEqual(self.exercises.list_product([-1, 2, 3]), -6)
        
if __name__ == '__main__':
    unittest.main()
