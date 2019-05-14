"""Functions to work with divisibles"""

def is_divisible(x, y):
    """Checks if a number is divisible by another

    Arguments:
        x (int): Divisor of the operation.
        y (int): Dividend of the operation.

    Returns:
        True if x can be divided by y without reminder,
        False otherwise.

    Raises:
        :obj:`ZeroDivisionError` if y is 0.
    """
    if x % y == 0:
        return True
    else:
        return False
