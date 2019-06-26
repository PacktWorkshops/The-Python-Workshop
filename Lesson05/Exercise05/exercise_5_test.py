import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise05
        self.exercises = Exercise05

    def test_chubbles(self):
        self.assertTrue(self.exercises.bowser.is_tall())

        
if __name__ == '__main__':
    unittest.main()
   