from importnb import Notebook
import unittest

with Notebook():
    import Exercise01


class Test(unittest.TestCase):
    def test_cubes(self):
        assert(Exercise01.cubes == [1, 8, 27, 64, 125])


if __name__ == '__main__':
    unittest.main()
