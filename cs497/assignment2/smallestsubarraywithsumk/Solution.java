package cs497.assignment2.smallestsubarraywithsumk;

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