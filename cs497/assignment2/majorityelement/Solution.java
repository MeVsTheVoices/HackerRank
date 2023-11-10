package cs497.assignment2.majorityelement;
// This is going to be an implementation of Moores Voting Algorithm

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