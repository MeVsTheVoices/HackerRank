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

def griddy(firstLine, secondLine, r, c):
    if r == 1:
        return firstLine[c-1]
    elif r == 2:
        return secondLine[c-1]
    else:
        return griddy(
            [x + 10 for x in firstLine],
            [x + 10 for x in secondLine],
            r - 2,
            c
        )


def strangeGrid(r, c):
    return griddy([x for x in range (0, 9, 2)], [x for x in range (1, 10, 2)], r, c)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
