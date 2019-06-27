import unittest
import import_ipynb
import datetime
import multiply

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply.list_product([2, 10]), 20)
        
if __name__ == '__main__':
    unittest.main()
