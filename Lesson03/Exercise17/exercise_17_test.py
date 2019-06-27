import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise17
        self.exercises = Exercise17

    def test(self):
        self.exercises.countdown(3)
        
if __name__ == '__main__':
    unittest.main()
