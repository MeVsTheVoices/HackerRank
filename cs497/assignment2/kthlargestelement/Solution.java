package cs497.assignment2.kthlargestelement;

import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> kTracker = new PriorityQueue<Integer>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            kTracker.offer(num);
            if (kTracker.size() > k)
                kTracker.poll();
        }
    
        return kTracker.poll();
    }
}