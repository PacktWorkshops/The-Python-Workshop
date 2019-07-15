from importnb import Notebook
import unittest
import math

with Notebook():
    import Activity03


class Test(unittest.TestCase):
    def test_pi_estimate(self):
        # Expect the estimates to be between 3.0 and 3.2. It won't always be true, but it will often be true.
        for e in Activity03.estimates:
            error = math.fabs(e - math.pi)
            assert(error < 0.1)

    def test_pi_error(self):
        for i in range(len(Activity03.estimates)):
            estimate = Activity03.estimates[i]
            error = Activity03.errors[i]
            assert(estimate + error - math.pi < 1e4)


if __name__ == '__main__':
    unittest.main()
