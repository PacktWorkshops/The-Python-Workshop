import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise09
        self.exercises = Exercise09

    def test(self):
        self.assertEqual(self.exercises.get_second_element([1]), 'List was too small')
        self.assertEqual(self.exercises.get_second_element([1, 2, 3]), 2)

if __name__ == '__main__':
    unittest.main()
