# Testing
Testing is at python_testing/stringtointeger_test.py

# Intuition
This is mostly a simple problem. Instead of two iterations, one to find the greatest power, then working left to right, we work right to left and increase the power of ten by one every time we find a numerical character. If we find a nonnumerical character, we reset the value and the power counters, then continue. We also have to check for the sign of the number, and we have to check for overflow.

# Approach
    1. Define bounds
    2. Strip whitespace
    3. Check for sign
    4. Iterate right to left
        1. Check for numerical character
            1. Add to value
            2. Increase power
        2. Else
            1. Reset value
            2. Reset power

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(1)$$

# Code
```
class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT = -pow(2, 31)
        MAX_INT = pow(2, 31) - 1
        stripped = s.strip()
        if len(stripped) < 1:
            return 0
        positive = True
        position = 0
        if stripped[0] == '+':
            positive = True
            position += 1
        elif stripped[0] == '-':
            positive = False
            position += 1
        elif not stripped[0].isnumeric():
            return 0
        power = 0
        value = 0
        for i in range(len(stripped) - 1, position - 1, -1):
            character = stripped[i]
            if character.isnumeric():
                value += pow(10, power) * int(character)
                power += 1
            else:
                power = 0
                value = 0
        value = value if positive else -value
        if value < MIN_INT:
            value = MIN_INT
        elif value > MAX_INT:
            value = MAX_INT
        return value
```