#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY operations
#

def solve(n, operations):
    # Write your code here
    numberOfJars = n
    
    totalAmount = 0
    for i in operations:
        span = (i[1] - i[0]) + 1
        spannedAmount = span * i[2]
        totalAmount += spannedAmount
        
    return totalAmount / numberOfJars

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = int(solve(n, operations))

    fptr.write(str(result) + '\n')

    fptr.close()
