class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
    def binarySearch(self, arr, x):
        return self.binarySearchHelper(arr, x, 0, len(arr) - 1)
    
    def binarySearchHelper(self, arr, x, left, right):
        left, right = 0, len(arr) - 1
        mid = (left + right) // 2
        print(left, right, mid)
        if left == right:
            return left
        elif arr[mid] > x:
            right = mid - 1
            return self.binarySearchHelper(arr, x, left, right)
        elif arr[mid] < x:
            left = mid + 1
            return self.binarySearchHelper(arr, x, left, right)
        else:
            return mid