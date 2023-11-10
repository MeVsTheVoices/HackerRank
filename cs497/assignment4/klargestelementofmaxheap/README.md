# Testing
Testing is at python_testing\klargestelementsofmaxheap_test.py

# Intuition
We use a priority queue to keep track of where we are, then append results as we go, keeping a set to ensure we don't add things twice.

# Approach
- Initialize a minheap with the first element of the array
- Initialize a set to keep track of the indices we've added to the heap
- Initialize a list to keep track of the results
- While we haven't added k elements to the results
    - Pop the smallest element from the heap
    - Add it to the results
    - Add its left and right children to the heap if they haven't been added yet

# Complexity
- Time complexity: O(n)
- If we imagine a heap [50, 49, 48, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], we can see that we only have to add the first 3 elements to the heap, then we can just pop the smallest element and add its children to the heap. This means that we only have to add n/2 elements to the heap, which is O(n). The rest of the operations are O(1), so the total time complexity is O(n + n/2) = O(n)

- Space complexity: O(n)
- The worst case is where we have to add all the elements to the heap, which is O(n)

# Code
```
from heapq import heappush, heappop

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = []
        heap = []
        added_indices = set()
        heappush(heap, (-nums[0], 0))
        added_indices.add(0)
        i = 0
        while i < k:
            value, index = heappop(heap)
            res.append(-value)
            left = 2 * index + 1
            right = 2 * index + 2
            if left < len(nums) and left not in added_indices:
                heappush(heap, (-nums[left], left))
                added_indices.add(left)
            if right < len(nums) and right not in added_indices:
                heappush(heap, (-nums[right], right))
                added_indices.add(right)
            i += 1

        return res

```