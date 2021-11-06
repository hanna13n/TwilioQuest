import sys

args = sys.argv
args.pop(0)

for i in args:
    f = 0
    if int(i) % 3 == 0:
        print("fizz", end="")
        f = 1
    if int(i) % 5 == 0:
        print("buzz", end="")
        f = 1
    if f == 0:
        print(i, end="")
    print("\n", end="")
