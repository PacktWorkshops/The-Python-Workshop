import unittest
import import_ipynb
import datetime
import numpy as np

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise08
        self.exercises = Exercise08

    def test_sum(self):
        self.assertEqual(self.exercises.housing_df.shape, (506, 14))
        
if __name__ == '__main__':
    unittest.main()
   