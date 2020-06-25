import argparse

parser = argparse.ArgumentParser(description="Interpret a Boolean flag.")
parser.add_argument('--flag', dest='flag', action='store_true', help='Set the flag value to True.')
arguments = parser.parse_args()
print(f"The flag's value is {arguments.flag}")
