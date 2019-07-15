import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise06
        self.exercises = Exercise06

    def test(self):
        self.assertEqual(self.exercises.l, [1, 2, 3, 5, 8])
        
if __name__ == '__main__':
    unittest.main()
