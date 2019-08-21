import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise02
        self.exercises = Exercise02

    def test_chubbles(self):
        self.assertEqual(self.exercises.chubbles.owner, 'Michael Smith')

        
if __name__ == '__main__':
    unittest.main()
