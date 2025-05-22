#!/usr/bin/env python3

import sys

# Check if exactly 2 additional arguments are provideed 
if len(sys.argv) != 3:
    # print  usage message 
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# arguments assigned to variable 
name = sys.argv[1]
age = sys.argv[2]

# Print the greeting 
print(f"Hi {name}, you are {age} years old.")

