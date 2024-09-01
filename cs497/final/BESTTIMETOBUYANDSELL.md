# Intuition
We want to break this down in to a dynamic programming problem. To do so, we need to find the subproblems. In this case, we can think of the subproblem as the maximum profit we can make at each day. We can then use this to find the maximum profit we can make at the end of the day.

# Approach
- Create n buckets to store the maximum profit we can make at each day
- Iterate from [1, n]
  - Update the maximum profit we can make at each day
  - Update the minimum price we can buy at each day
- Return the maximum profit.

# Complexity
- Time complexity: O(n)
  - Despite the approach, we're still examining each day once, so O(n)

- Space complexity: O(n)
    - We store n integers in the maximumProfit array, so O(n)

# Code
```
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Use dynamic programming to solve this problem
        n = len(prices)
        if n == 0:
            return 0
        maximumProfit = [0] * n
        minimumPrice = prices[0]
        for i in range(1, n):
            maximumProfit[i] = max(maximumProfit[i-1], prices[i] - minimumPrice)
            minimumPrice = min(minimumPrice, prices[i])
        return maximumProfit[-1]
```