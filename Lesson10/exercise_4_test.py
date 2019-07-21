import unittest
import import_ipynb
import datetime
import numpy as np

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise04
        self.exercises = Exercise04

    def test_sum(self):
        self.assertAlmostEqual(self.exercises.new_array.sum(), 210)
        
if __name__ == '__main__':
    unittest.main()
   