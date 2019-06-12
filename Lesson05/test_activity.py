import unittest
import import_ipynb
import datetime

class TestActivity(unittest.TestCase):
    def test_rectangle(self):
        import activity
        self.assertEqual(activity.r.area, 5)
        self.assertEqual(activity.r.perimeter, 12)
        
    def test_square(self):
        import activity
        self.assertEqual(activity.s.area, 25)
        self.assertEqual(activity.s.perimeter, 20)

if __name__ == '__main__':
    unittest.main()