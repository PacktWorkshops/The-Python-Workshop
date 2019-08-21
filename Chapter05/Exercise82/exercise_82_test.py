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
        self.assertEqual(self.exercises.d.add_days(400), datetime.date(2021,1,4))

        
if __name__ == '__main__':
    unittest.main()
