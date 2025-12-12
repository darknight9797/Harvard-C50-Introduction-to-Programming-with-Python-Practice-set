import sys

try:
    print("my name is", sys.argv[1])

except IndexError:
    print("No name provided")
