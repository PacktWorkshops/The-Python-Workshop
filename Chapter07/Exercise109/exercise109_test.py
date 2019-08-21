from importnb import Notebook
import unittest

with Notebook():
    import Exercise11


class Test(unittest.TestCase):
    def test_prime_generator(self):
        primes = [p for p in Exercise11.primes_below(10)]
        assert(primes == [2, 3, 5, 7])


if __name__ == '__main__':
    unittest.main()
