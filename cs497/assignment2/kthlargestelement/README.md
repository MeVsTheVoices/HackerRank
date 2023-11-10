# Intuition
Instead of using a list, we keep a priority queue for the largest elements, if we have more than k elements, we pop the smallest, we get linear removal time and logarithmic insertion time because of the use of data structures

# Approach
Java doesn't have a native evicting queue, which would have been ideal, we only need to keep the kth largest elements to compare against, so, every time we iterate, we offer the element to the priorrity queue, and evict the smallest element iff we have k larger elements.

# Complexity
- Time complexity: O(n)

- Space complexity: O(k)

# Code
```
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
```