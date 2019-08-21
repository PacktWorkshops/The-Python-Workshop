from importnb import Notebook
import unittest

with Notebook():
    import Activity02


class Test(unittest.TestCase):
    def test_scores(self):
        expected_scores = {'Vivian Smith-Smythe-Smith': 20, 'Simon Zinc-Trumpet-Harris': 130,
                           'Nigel Incubator-Jones': 80, 'Gervaise Brook-Hamster': 100}
        assert(Activity02.scores == expected_scores)


if __name__ == '__main__':
    unittest.main()
