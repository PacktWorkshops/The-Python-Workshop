import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise24
        self.exercises = Exercise24

    def test(self):
        nums = list(range(1000))
        self.assertEqual(sum(filter(lambda x: x % 3 == 0 or x % 7 == 0, nums)), 214216)
        
if __name__ == '__main__':
    unittest.main()
