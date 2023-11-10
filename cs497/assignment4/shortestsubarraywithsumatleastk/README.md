# Intuition
We keep a doubly linked list, we add to the right while the sum we're examining is less than the sum we're attempting to reach. We remove from the left while the sum we're examining is greater than the sum we're attempting to reach. We keep track of the minimum sum we've seen so far. We keep track of the shortest subarray we've seen so far. We return the shortest subarray we've seen so far.

# Approach
  - We keep a doubly linked list, we add to the right while the sum we're examining is less than the sum we're attempting to reach.
  - We remove from the left while the sum we're examining is greater than the sum we're attempting to reach.
  - We keep track of the minimum sum we've seen so far.
  - We keep track of the shortest subarray we've seen so far.
  - We return the shortest subarray we've seen so far.

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```
from collections import deque
import math


class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        dq = deque()
        shortest = math.inf
        current_sum = 0
        min_sum = 0
        
        for i in range(size):
            current_sum += nums[i]
            
            if current_sum - min_sum >= k:
                shortest = min(shortest, i + 1)
            
            while dq and current_sum - dq[0][1] >= k:
                shortest = min(shortest, i - dq[0][0])
                dq.popleft()
            
            while dq and current_sum <= dq[-1][1]:
                dq.pop()
            
            dq.append((i, current_sum))
            min_sum = min(min_sum, current_sum)
        
        return shortest if shortest != math.inf else -1
        
```