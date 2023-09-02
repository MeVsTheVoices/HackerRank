#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#


def strangeGrid(r, c):
    if ((r - 1) % 2) == 0:
        offset = 0
    else:
        offset = 1
    r = r - 1
    return (r // 2) * 10 + (c - 1) * 2 + offset

if __name__ == '__main__':
    sys.setrecursionlimit(235345342)
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
