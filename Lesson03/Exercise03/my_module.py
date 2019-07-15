"""This script computes the sum of the factorial of a list of numbers"""

import math

def compute(numbers):
    return sum([math.factorial(n) for n in numbers])