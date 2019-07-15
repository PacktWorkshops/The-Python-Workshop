import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise02
        self.exercises = Exercise02

    def test(self):
        self.assertEqual(self.exercises.compute([5, 7, 11]), [120, 5040, 39916800])
        
if __name__ == '__main__':
    unittest.main()
