# Testing
Testing is at python_testing/hammingdistance_test.py

# Intuition
Keep shifting and taking the lowest digit, if the XOR of the two lowest digits is 1, then increment the distance counter.

# Approach
    - Define a variable a zero
    - Take the lowest binary digit of x and y
    - If the XOR of the two lowest digits is 1, then increment the distance counter
    - Shift x and y to the right by 1 and continue do so while they are greater than 0
    - Return the distance counter

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distanceSoFar = 0
        while x or y:
            lowestBitOfX = x % 2
            lowestBitOfY = y % 2
            print(lowestBitOfX, " ", lowestBitOfY)
            if lowestBitOfX ^ lowestBitOfY:
                distanceSoFar += 1
            x >>= 1
            y >>= 1
        return distanceSoFar
```