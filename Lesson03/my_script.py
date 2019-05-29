"""This script computes the sum of the factorial of a list of numbers"""

import math

numbers = [5, 7, 11]

result = sum([math.factorial(n) for n in numbers])

print(result)
