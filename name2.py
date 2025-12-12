import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

print("hello,", sys.argv[1]) 