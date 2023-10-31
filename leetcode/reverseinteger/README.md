# Intuition
A cheaty cheater used a string.

# Approach
I used integer arithmetic to do another, now we're taking the simpler approach
    - Convert the integer to a string.
    - Reverse the string.
    - Convert the string back to an integer.
    - If the integer is out of bounds, return 0.

# Complexity
- Time complexity: O(1)

- Space complexity: O(1)

# Code
```
class Solution:
    def reverse(self, x: int) -> int:
        MAX_BOUND = ((pow(2, 31)) - 1)
        MIN_BOUND = -(pow(2, 31))
        print(MAX_BOUND, MIN_BOUND)
        isNegative = False
        if x < 0:
            isNegative = True
        print(x)
        xAsAString = str(x)
        if isNegative:
            xAsAString = xAsAString[1:]
            x = -int(xAsAString[::-1])
        else:
            x = int(xAsAString[::-1])
        print(x)
        if (x < MIN_BOUND) or (x > MAX_BOUND):
            return 0
        return x
```