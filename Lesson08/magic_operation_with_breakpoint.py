# This is a comment

this = "is the first line to execute"

def secret_sauce(number):
    breakpoint()
    if number <= 10:
        return number + 10
    else:
        return number - 10

def magic_operation(x, y):
    res = x + y
    res *= y
    res /= x
    res = secret_sauce(res)
    return res

print(magic_operation(2, 10))
