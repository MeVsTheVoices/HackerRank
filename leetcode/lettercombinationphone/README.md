# Intuition
Given a sequence of numbers 2-9 and corresponding letters on a phone keypad, return all possible letter combinations that the numbers could represent.

# Approach
1. Create a dictionary that maps each number to its corresponding letters.
2. Create a list of lists where each list is the list of letters corresponding to each number in the input string.
3. Use itertools.product to get the cartesian product of the list of lists.
4. Convert the cartesian product to a list of strings.

# Complexity
- Time complexity: O(x^n) where x is the average number of letters per number and n is the length of the input string.

- Space complexity: O(x^n) where x is the average number of letters per number and n is the length of the input string.

# Code
```
import itertools

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
```