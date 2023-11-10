# Intuition
Use binary search to find the element closest to the element sepcified. Then travel left and right of that element k elements.

# Approach
    - Implement binary search
    - Use binary search to find the closest element p
    - Traverse between p - k and p + k, record the differences between those and x
    - Sort based on the differences
    - Return the first k elements

# Complexity
- Time complexity: max(log(n), klog(k))
    - We implement binary search O(log(n))
    - We traverse k*2 elements
    - We sort k*2 elements

- Space complexity: O(k)

# Code
```
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        closest = self.binarySearch(arr, x)
        lower = 0 if closest - k < 0 else closest - k
        upper = len(arr) - 1 if closest + k > len(arr) - 1 else closest + k
        pairs = []
        for i in range(lower, upper + 1):
            pairs.append((abs(arr[i] - x), arr[i]))
        pairs.sort()
        result = []
        for i in range(k):
            result.append(pairs[i][1])
        result.sort()
        return result

    def binarySearch(self, arr, x):
        return self.binarySearchHelper(0, len(arr) - 1, arr, x)
        
    def binarySearchHelper(self, low, high, arr, x):
        mid = (high + low) // 2
        if high >= low:

            if arr[mid] == x:
                return mid
            else:
                if arr[mid] > x:
                    return self.binarySearchHelper(low, mid - 1, arr, x)
                else:
                    return self.binarySearchHelper(mid + 1, high, arr, x)
        else:
            return mid
```