import unittest
import import_ipynb
import datetime
import numpy as np

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise01
        self.exercises = Exercise01

    def test_median(self):
        self.assertEqual(np.median(self.exercises.income), 88000)
        
    def test_mean(self):
        self.assertAlmostEqual(np.mean(self.exercises.income), 1786285.7142857143)
        
if __name__ == '__main__':
    unittest.main()
   