from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(range(1, len(nums) + 1))
        duplicate = 0
        for i in nums:
            if i not in s:
                duplicate = i
            else:
                s.remove(i)
        return [duplicate, list(s).pop()]