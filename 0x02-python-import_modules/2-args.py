#!/usr/bin/python3
if __name__ == "__main__":
    import sys

args = sys.argv[1:]
num_args = len(args)
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_args))

if num_args >= 1:
    i = 0
    for arg in range(args):
        print("{}: {}".format(i, arg))
        i += 1
