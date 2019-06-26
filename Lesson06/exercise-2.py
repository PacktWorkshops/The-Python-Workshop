import argparse
parser = argparse.ArgumentParser(description="""
Prints out the words passed in, capitalizes them if required
and repeat them in as many lines as requested.
""")
parser.add_argument("message", help="Messages to be echoed", nargs="+")
parser.add_argument("-c", "--capitalize", action="store_true")
parser.add_argument("--repeat", type=int, default=1)
args = parser.parse_args()
if args.capitalize:
    messages = [m.capitalize() for m in args.message]
else:
    messages = args.message
for _ in range(args.repeat):
    print(" ".join(messages))
