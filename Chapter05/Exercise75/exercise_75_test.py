import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise06
        self.exercises = Exercise06

    def test_algeria_size(self):
        self.assertAlmostEqual(self.exercises.algeria.size_miles_sq(conversion_rate=0.6), 857520.0)

        
if __name__ == '__main__':
    unittest.main()
   