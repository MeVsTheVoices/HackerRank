from functools import reduce
import itertools
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []
        numbersToLetters = {
            1: [],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        possibilities = [numbersToLetters[int(x)] for x in list(digits)]
        cartesianProduct = itertools.product(*possibilities)
        stringified = []
        for x in cartesianProduct:
            stringified.append(reduce(lambda m, n: m + n, x, ""))

        return stringified