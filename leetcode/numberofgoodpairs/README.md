# Intuition
All we're doing her is adding the indices to a list in a hashmap

# Approach
Go through for i in list, each time we have a new number, we add the index for that number to the list stored at the value in the hash map.
As we're looking only for identically valued integers, we can store these indexes under the same key to work with later.
Subsequently, we iterate through all the keys in the map, for each of these, we then loop through for each subsequent index, if the index at k+1, k+2, ... is greater than the index k, we count upwards

# Complexity
- Time complexity: O(n^2)
Conceptualize it this way. Insertion in a hashmap is O(1). We iterate first O(n). Say for example we were given a list of identical values. For each n, n - 1, n - 2, ..., we'd iterate n - 1, n - 2, n - 3, ... times.

- Space complexity: O(n)
We have one entry in each list for each index, thus, O(n)

# Code
```
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        listOfIndices = {}
        for i, value in enumerate(nums):
            if value in listOfIndices:
                listOfIndices[value] = listOfIndices[value] + [i]
            else:
                listOfIndices[value] = [i]
        print(listOfIndices)
        countOfGoodIndices = 0
        for value in listOfIndices:
            print(str(value))
            for index, initialIndex in enumerate(listOfIndices[value]):
                for subsequentIndex in listOfIndices[value][index + 1:]:
                    if initialIndex < subsequentIndex:
                        countOfGoodIndices += 1
        return countOfGoodIndices
```