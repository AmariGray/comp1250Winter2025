import sys
import os

# sys.argv  # a list of arguments

"""
    0:      file name
    1: a value after the file name
"""

if len(sys.argv) != 3:
    print(f"Error! Incorrect Usage of "
          f"{os.path.basename(sys.argv[0])}",
          file=sys.stderr)
    sys.exit("Exiting script because you did not follow the instructions")


num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(f"{num1} + {num2} = {num1 + num2}")
