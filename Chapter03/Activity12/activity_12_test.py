import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def test(self):
        import Activity05
        self.assertEqual(Activity05.fibonacci_dynamic(100), 354224848179261915075)
        
if __name__ == '__main__':
    unittest.main()
