import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise14
        self.exercises = Exercise14

    def test(self):
        self.assertEqual(self.exercises.second_diary.show_christmas(), '03/03/2018')

        
if __name__ == '__main__':
    unittest.main()
