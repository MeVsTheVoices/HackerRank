from typing import *

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNumbers = nums.copy()
        sortedNumbers.sort(reverse=True)
        sortedNumbersMap = {}
        for i, j in enumerate(sortedNumbers):
            sortedNumbersMap[j] = len(sortedNumbers) - i - 1

        return [sortedNumbersMap[i] for i in nums]

        