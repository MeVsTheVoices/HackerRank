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