import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise21
        self.exercises = Exercise21

    def test(self):
        self.assertEqual(self.exercises.compute_usd_total(amount_in_gbp=10), 13.029)
        
if __name__ == '__main__':
    unittest.main()
