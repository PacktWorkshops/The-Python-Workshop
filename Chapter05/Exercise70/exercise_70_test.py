import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise01
        self.exercises = Exercise01

    def test_my_str(self):
        self.assertEqual(self.exercises.my_str, 'hello world!')

        
if __name__ == '__main__':
    unittest.main()
   