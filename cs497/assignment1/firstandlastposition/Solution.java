package firstandlastposition;

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