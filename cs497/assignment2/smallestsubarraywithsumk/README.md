# Intuition
This is the brute force solution. We can better using another approach, and I intend on coming back to this to better wrap my head around what's going on. For now, I'm moving on to the next problem. This is the naive O(n^2) solution.

# Approach
We're going to try every possible contiguous subset to check, if that subset has a sum greater than or equal to k. If it does, we'll check if it's the smallest subset we've found so far. If it is, we'll update the minimum length.


# Complexity
- Time complexity: O(n^2)

- Space complexity: O(1)

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