# Intuition
Break in to halves, then search each half recursively

# Approach
- Define a recursive helper function
    - It takes two pointers, left and right
    - If the two pointers are passed one another, the element isn't in the array
    - If the target element is at the mid point, return that
    - If the mid point is greater than the target, call recusrively on the bottom half
    - If the mid point is less than the target, call recursively on the top half

# Complexity
- Time complexity: O(log(n))
    - For each array of length 2*n, we'd have at most 1 more call

- Space complexity: O(n)

# Code
```
class Solution {
    public int search(int[] nums, int target) {
        return binarySearch(nums, target, 0, nums.length - 1);
    }

    private int binarySearch(int[] nums, int target, int start, int end) {
        if (start > end) return -1;
        int mid = (start + end) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] > target) 
            return binarySearch(nums, target, start, mid - 1);
        else
            return binarySearch(nums, target, mid + 1, end);
    }
}
```