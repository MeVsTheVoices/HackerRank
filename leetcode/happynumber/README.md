# Intuition
Because each step is uniquely determined by the one prior, we can simply keep track of those computed previously

# Approach
Caluclate the sum of squares of each, compare against a set, insert if not found within, break if we get a sum of squares equivalent to 1

# Complexity
- Time complexity: O(n^2)

- Space complexity: O(n)

# Code
```python3 []
class Solution:
    def isHappy(self, n: int) -> bool:
        haveSeen = set()
        sumSoFar = 0
        while self.sumOfSquares(n) not in haveSeen and self.sumOfSquares(n) != 1:
            haveSeen.add(self.sumOfSquares(n))
            n = self.sumOfSquares(n)
        return self.sumOfSquares(n) == 1

    def sumOfSquares(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += (n % 10) ** 2
            n //= 10
        return sum

```