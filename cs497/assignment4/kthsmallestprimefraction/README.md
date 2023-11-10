# Testing
Testing is at python_testing/kthsmallestprimefraction_test.py

# Intuition
We're using a minheap to track which are the smallest prime fractions.

# Approach
We iterate n^2 times, we add to a minheap with the key being the fraction. Then we take the k smallest in that minheap and return the numerator and denomenator.

# Complexity
- Time complexity: O(n^2)
    - We iterate n by n times to populate the minheap

- Space complexity: O(n^2)

# Code
```
from heapq import heappush, heappop, nsmallest

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []

        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                numerator = float(arr[i])
                denominator = float(arr[j])
                result = float(numerator/denominator)
                heappush(heap, [result,[arr[i],arr[j]]])

        return nsmallest(k, heap)[-1][-1]
```