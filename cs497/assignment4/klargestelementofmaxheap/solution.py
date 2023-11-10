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
