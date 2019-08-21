from importnb import Notebook
import unittest

with Notebook():
    import Exercise07


class Test(unittest.TestCase):
    def test_prime_generator(self):
        primes = [p for p in Exercise07.PrimesBelow(10)]
        assert(primes == [2, 3, 5, 7])


if __name__ == '__main__':
    unittest.main()
