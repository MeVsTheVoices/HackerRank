# Find First and Last Position of Element in Sorted Array

## Intuition
We're given a sorted array of integer and asked to find the first and last indexes of a particular element within. The specification lists O(log n) as the time complexity, which is a hint that we should be using a binary search algorithm. The problem is that we're looking for the first and last index of a particular element, which means we can't just return the index of the first element we find, we need to keep searching until we find the last index of the element.

## Approach
I first tried to use a regular binary search, then use the results of this function to find the first and last indexes of the element. This approach worked, but it was O(2 log n) which is not what we're looking for. I then tried to modify the binary search algorithm to find the first and last indexes of the element, but I couldn't get it to work. I then looked at the solution and found that it was a simple modification of the binary search algorithm. The solution is to use a binary search algorithm to find the first index of the element, then use a binary search algorithm to find the last index of the element. The only difference between the two is that the first binary search algorithm returns the index of the element if it finds it, and the second binary search algorithm returns the index of the element if it finds it, or the index of the element if it doesn't find it.

## Complexity
- Time complexity: O(log(n))
- Space complexity: O(1)

## Code
>
    class Solution {
        public int[] searchRange(int[] nums, int target) {
            // find the center
            if (nums.length == 0)
                return new int[] {-1, -1};
                
            int bottom = leftBound(nums, target, 0, nums.length - 1);
            int top = rightBound(nums, target, 0, nums.length - 1);
            //bottom half

            if (nums[bottom] != target)
                return new int[] {-1, -1};

            return new int[] {bottom, top};
        }

        public int leftBound(int[] nums, int target, int start, int end) {
            if (start == end)
                return start;
            int center = (start + end) / 2;
            if (nums[center] < target)
                return leftBound(nums, target, start + 1, end);
            else 
                return leftBound(nums, target, start, center);
        }
        
        public int rightBound(int[] nums, int target, int start, int end) {
            if (start == end)
                return start;
            int center = (start + end) / 2 + 1;
            if (nums[center] > target)
                return rightBound(nums, target, start, end - 1);
            else 
                return rightBound(nums, target, center, end);
        }

    }
    