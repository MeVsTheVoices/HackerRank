# Intuition
Copy that list. Sort the result. Iterate through. Then relate back.

# Approach
Make a copy of the list, then sort that.
Iterate through the sorted list, and store the number of elements that are smaller than it, (n - 1) for each n in a map.
Go through the original list one more time, and for each element in it, use the map to find the number of elements smaller than it.

# Complexity
- Time complexity: O(n*log(n))
    - Bounded by the sorting function

- Space complexity: O(n)

# Code
```
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNumbers = nums.copy()
        sortedNumbers.sort(reverse=True)
        sortedNumbersMap = {}
        for i, j in enumerate(sortedNumbers):
            sortedNumbersMap[j] = len(sortedNumbers) - i - 1

        return [sortedNumbersMap[i] for i in nums]

        
```