"""This script computes the factorial for a list of numbers"""

import math

def compute(numbers):
    return sum([math.factorial(n) for n in numbers])