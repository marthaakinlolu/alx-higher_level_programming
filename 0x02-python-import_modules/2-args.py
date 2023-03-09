#!/usr/bin/python3
if __name__ == "__main__":
    import sys
args = sys.argv[1:]
num_args = len(args)
    
if num_args == 0:
    print("{} arguments.".format(num_args))
elif num_args == 1:
    print("{} argument:".format(num_args))
else:
    print("{} arguments:".format(num_args))

if num_args >= 1:
    i = 1
    for arg in args:
        print("{}: {}".format(i, arg))
        i += 1
