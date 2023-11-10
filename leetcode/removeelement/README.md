# Testing
Testing is at python_testing\removeelement_test.py

# Intuition
We use two pointers, one keeps track of the number of element added to the array that are not equal to the target value, the other one iterates through the array. When the second pointer finds an element that is not equal to the target value, we add it to the array and increment the first pointer.

# Approach
    - Initialize a pointer to 0
    - Iterate through the array
        - If the element is not equal to the target value
            - Add it to the array at the index of the first pointer
            - Increment the first pointer
    - Return the first pointer

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for element in nums:
            if element != val:
                nums[index] = element
                index += 1
        return index
```