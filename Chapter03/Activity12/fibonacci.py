def fibonacci_iterative(n):
    previous = 0
    current = 1
    for i in range(n - 1):
        current_old = current
        current = previous + current
        previous = current_old
    return current
stored = {0: 0, 1: 1}  # We set the first 2 terms of the Fibonacci sequence here.
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)
def fibonacci_dynamic(n):
    if n in stored:
        return stored[n]
    else:
        stored[n] = fibonacci_dynamic(n - 2) + fibonacci_dynamic(n - 1)
        return stored[n]
