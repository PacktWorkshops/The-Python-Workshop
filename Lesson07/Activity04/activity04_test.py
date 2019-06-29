from importnb import Notebook
import unittest

with Notebook():
    import Activity04


class Test(unittest.TestCase):
    def test_winners(self):
        expected_winners = ['Xander Harris', 'Amy Alexandrescu', 'Weifung Xu']
        assert(Activity04.winners == expected_winners)


if __name__ == '__main__':
    unittest.main()
