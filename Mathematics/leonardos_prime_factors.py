#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#



def wilsons_theorem(n):
    return (math.factorial(n-1)+1)%n == 0

def generate_primes(n):
    return [i for i in range(1, n) if wilsons_theorem(i)]

if __name__ == '__main__':
    #specific to hackerrank
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #specific to local
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
