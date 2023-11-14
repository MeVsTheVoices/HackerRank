# Intuition
Use a set, then work backwards, delete from it to find the duplicate, then pop the remaining element to find the missing element.

# Approach
    - Create a set of all numbers from 1 to n
    - Traverse given array
        - If number is not in set, it is the duplicate
        - Else, remove it from the set
    - Return the duplicate and the remaining element in the set

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```
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
```