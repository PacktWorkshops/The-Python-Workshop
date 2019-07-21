import unittest
import import_ipynb
import datetime
import numpy as np

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise07
        self.exercises = Exercise07

    def test_sum(self):
        self.assertAlmostEqual(sum(self.exercises.housing_df.head().iloc[0]), 834.89932)
        
if __name__ == '__main__':
    unittest.main()
   