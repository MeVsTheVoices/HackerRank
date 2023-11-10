class Solution(object):
    def findClosestElements(self, arr, k, x):
            """
            Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
            The result should also be sorted in ascending order.

            :param arr: A sorted list of integers
            :type arr: List[int]
            :param k: The number of closest elements to return
            :type k: int
            :param x: The target integer
            :type x: int
            :return: A list of the k closest integers to x in arr, sorted in ascending order
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
        """
        Helper function for binary search algorithm.

        Args:
        low (int): The lowest index of the search range.
        high (int): The highest index of the search range.
        arr (List[int]): The sorted array to search.
        x (int): The value to search for.

        Returns:
        int: The index of the element in the array that matches the search value, or the index of the closest element if the search value is not found.
        """
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