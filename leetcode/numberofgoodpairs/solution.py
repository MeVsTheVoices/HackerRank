from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        listOfIndices = {}
        for i, value in enumerate(nums):
            if value in listOfIndices:
                listOfIndices[value] = listOfIndices[value] + [i]
            else:
                listOfIndices[value] = [i]

        countOfGoodIndices = 0
        for value in listOfIndices:
            for index, initialIndex in enumerate(listOfIndices[value]):
                for subsequentIndex in listOfIndices[value][index + 1:]:
                    if initialIndex < subsequentIndex:
                        countOfGoodIndices += 1
        return countOfGoodIndices