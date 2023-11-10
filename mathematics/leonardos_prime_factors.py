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

def generate_n_primes(n):
    primes = []
    i = 1
    while len(primes) < n:
        if wilsons_theorem(i):
            primes.append(i)
        i += 1
    return primes

def generate_n_primes_static(n):
    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 
103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 
223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 
347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 
463, 467, 479, 487, 491, 499, 503, 509, 521, 523]
    return primes[:n]

def all_multiples_less_than_n(j, n):
    return [i*j for i in range(1, n // j)]

def eratosthenes_sieve(n):
    primes = []
    multiples = []
    for i in range(2, n):
        if i not in multiples:
            primes.append(i)
            multiples.extend(all_multiples_less_than_n(i, n))
    return primes

def primeCount(n):
    if (n == 1):
        return 0
    number_of_primes = 1
    primes = generate_n_primes_static(number_of_primes)
    while math.prod(primes) <= n:
        number_of_primes += 1
        primes = generate_n_primes_static(number_of_primes)
    return number_of_primes - 2



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

