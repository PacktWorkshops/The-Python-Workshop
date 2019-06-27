import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise18
        self.exercises = Exercise18

    def test(self):
        self.assertEqual(self.exercises.factorial_iterative(5), 120)
        self.assertEqual(self.exercises.factorial_recursive(5), 120)

if __name__ == '__main__':
    unittest.main()
