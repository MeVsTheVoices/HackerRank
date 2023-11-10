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