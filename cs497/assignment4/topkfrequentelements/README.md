# Testing
Testing is at python_testing/topkfrequentelements_test.py

# Intuition
I'm switching over to Python. I might change back for quizes and midterms, but I haven't had a whole lot of experience with python weirdly, so, I'm going to try to do quite a few of these in python now. My intuition was very basic, I modified binary search slightly, instead of failing when it tries to find an element, it will just continue until the two pointers are equivalent.

# Approach
After using binary search to find a closest element, we then analyze k elements to its left and its right. We take the absolute value of those and the original elements in a tupple, and sort based on the differences. We find those closest, sort them, then return the result.

# Complexity
- Time complexity: max(log(n), klog(k))
    - Binary search is at first log(n)
    - We then compare and sort at most k * 2 elements

- Space complexity: O(n*log(n))
    - The worst case is where k * 2 >= n, in which case we're going to sort the entire array

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