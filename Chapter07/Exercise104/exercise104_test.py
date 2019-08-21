from importnb import Notebook
import unittest

with Notebook():
    import Exercise06


class Test(unittest.TestCase):
    def test_questions(self):
        questions = [q for q in Exercise06.awkward_person]
        assert(questions == ['What is your name?', 'What is your quest?',
                             'What is the average airspeed velocity of an unladen swallow?'])


if __name__ == '__main__':
    unittest.main()
