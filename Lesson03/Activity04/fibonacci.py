def fibonacci_iterative(n):
    previous = 0
    current = 1
    for i in range(n - 1):
        current_old = current
        current = previous + current
        previous = current_old
    return current
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)
