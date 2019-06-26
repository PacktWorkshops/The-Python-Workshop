import unittest
import import_ipynb
import datetime

class TestActivity(unittest.TestCase):
    def test_rectangle(self):
        import Activity01
        self.assertEqual(Activity01.r.area, 5)
        self.assertEqual(Activity01.r.perimeter, 12)
        
    def test_square(self):
        import Activity01
        self.assertEqual(Activity01.s.area, 25)
        self.assertEqual(Activity01.s.perimeter, 20)

if __name__ == '__main__':
    unittest.main()