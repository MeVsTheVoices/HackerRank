#!/bin/python3

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    #n = int(input().strip())
    n = 4444
    highest_score = 0
    best_divisor = 0
    for i in range(1, (n + 1)):
        if ((n % i) == 0):
            score = 0
            for j in str(i):
                score += int(j)
            if score > highest_score:
                highest_score = score
                best_divisor = i

    print(best_divisor)