import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise15
        self.exercises = Exercise15

    def test(self):
        self.assertEqual(self.exercises.sum_first_n(100), 5050)
        
if __name__ == '__main__':
    unittest.main()
