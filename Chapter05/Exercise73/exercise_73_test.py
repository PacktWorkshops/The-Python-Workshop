import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise04
        self.exercises = Exercise04

    def test(self):
        res = {'name': 'United States of America',
             'population': None,
             'size_kmsq': 9800000.0}
        self.assertEqual(self.exercises.usa.__dict__, res)

        
if __name__ == '__main__':
    unittest.main()
   