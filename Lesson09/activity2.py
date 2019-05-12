import argparse
parser = argparse.ArgumentParser(description="Play the game of FizzBuzz.")
parser.add_argument("fizz", action="store", help="Number to replace multiples of by 'Fizz'.", type=int)
parser.add_argument("buzz", action="store", help="Number to replace multiples of by 'Buzz'.", type=int)
arguments = parser.parse_args()
fizz = arguments.fizz
buzz = arguments.buzz
fizzbuzz = lambda x: "Fizzbuzz" if x%fizz == 0 and x%buzz == 0 else "Fizz" if x%fizz == 0 else "Buzz" if x%buzz == 0 else str(x)
print([fizzbuzz(i) for i in range(1,101)])
