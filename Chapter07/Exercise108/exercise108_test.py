from importnb import Notebook
import itertools
import unittest

with Notebook():
    import Exercise10


class Test(unittest.TestCase):
    def test_turns(self):
        local_counter = itertools.count(2, -1)
        turns = [t for t in itertools.takewhile(lambda x:next(local_counter) > 0, Exercise10.turns)]
        assert(turns == ['Black', 'White'])


if __name__ == '__main__':
    unittest.main()
