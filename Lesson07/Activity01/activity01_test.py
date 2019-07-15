from importnb import Notebook
import unittest

with Notebook():
    import Activity01


class Test(unittest.TestCase):
    def test_fixtures(self):
        games = Activity01.fixtures
        expected_games = ['Magnus Carlsen vs. Fabiano Caruana', 'Magnus Carlsen vs. Yifan Hou', 'Magnus Carlsen vs. Wenjun Ju', 'Fabiano Caruana vs. Magnus Carlsen', 'Fabiano Caruana vs. Yifan Hou', 'Fabiano Caruana vs. Wenjun Ju', 'Yifan Hou vs. Magnus Carlsen', 'Yifan Hou vs. Fabiano Caruana', 'Yifan Hou vs. Wenjun Ju', 'Wenjun Ju vs. Magnus Carlsen', 'Wenjun Ju vs. Fabiano Caruana', 'Wenjun Ju vs. Yifan Hou']
        assert(games == expected_games)


if __name__ == '__main__':
    unittest.main()
