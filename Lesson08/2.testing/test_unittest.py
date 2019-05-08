import unittest
from sample_code import is_divisible

class TestIsDivisible(unittest.TestCase):
    def test_divisible_numbers(self):
        self.assertTrue(is_divisible(10, 2))
        self.assertTrue(is_divisible(10, 10))
        self.assertTrue(is_divisible(1000, 1))

    def test_not_divisible_numbers(self):
        self.assertFalse(is_divisible(5, 3))
        self.assertFalse(is_divisible(5, 6))
        self.assertFalse(is_divisible(10, 3))

    def test_dividing_by_0(self):
        with self.assertRaises(ZeroDivisionError):
            is_divisible(1, 0)

if __name__ == '__main__':
    unittest.main()
