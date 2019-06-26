import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise15
        self.exercises = Exercise15

    def test(self):
        boris = self.exercises.OrganizedBaby('Boris', 'Bumblebutton')
        boris.book_appointment(datetime.date(2018,1,1))
        
if __name__ == '__main__':
    unittest.main()
