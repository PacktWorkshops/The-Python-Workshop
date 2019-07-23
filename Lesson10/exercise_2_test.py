import unittest
import import_ipynb
import datetime
import numpy as np

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise02
        self.exercises = Exercise02

    def test_sum(self):
        self.assertEqual(self.exercises.scores.sum(), 318)
        
if __name__ == '__main__':
    unittest.main()
   