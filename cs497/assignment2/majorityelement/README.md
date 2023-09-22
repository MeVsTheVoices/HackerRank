# Intuition
Because we're given the constraint that the element will occur atleast n/2 times, we can be assured that, if we keep a count of that element, and decrement when we find an unequal element, that element will 'win out', and will be the remaining element.

# Approach
We take the first element, then iterate over the remaining, the algorithm will hold, if we encounter the same element, we increase a counter, if the counter hits zero, then we replace the original element.

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```
class Solution {
    public int majorityElement(int[] nums) {
        int counter = 1;
        int element = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums [i] == element) {
                counter++;
            } else {
                counter--;
            }
            if (counter == 0) {
                element = nums[i];
                counter = 1;
            }
        }
        return element;
    }
}
```