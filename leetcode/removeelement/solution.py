from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for element in nums:
            if element != val:
                nums[index] = element
                index += 1
        return index