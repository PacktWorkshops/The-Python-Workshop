import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise13
        self.exercises = Exercise13

    def test(self):
        self.assertAlmostEqual(self.exercises.convert_usd_to_aud(100, rate=0.78), 128.2051282051282)
        
if __name__ == '__main__':
    unittest.main()
