# Intuition
Keep track of left and right bounds, split the tree in to two, then process each subtree recursively.

# Approach
There's nothing fancy here, we define a helper function that can be called recursively with the original array and two integer indices that keep track of left and right bounds. We create the root array, the process the left and right trees through two recursive calls. As the given array is already sorted, we process the left array from the right of the mid point, and process the right array from the right of the mid point.


# Complexity
- Time complexity: O(n)
- We visit each element only once

- Space complexity: O(log(n))
- The height of the resultant tree is log(n)


# Code
```
class Solution {
    public int shortestSubarray(int[] nums, int k) {
        int minimumLength = -1;
        int sum = 0;
        
        for (int i = 0; i < nums.length; i++) {
            sum = nums[i];
            if (sum >= k) {
                return 1;
            }
            for (int j = i + 1; j < nums.length; j++) {
                sum += nums[j];
                if (sum >= k) {
                    if (minimumLength == -1 || j - i + 1 < minimumLength) {
                        minimumLength = j - i + 1;
                    }
                    break;
                }
            }
        }
        return minimumLength;
    }
}
```