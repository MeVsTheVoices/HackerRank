package cs497.assignment1.TwoSum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

class Solution {


    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        AtomicInteger counter = new AtomicInteger(0);
        Arrays.stream(nums).forEach(num -> {
            map.put(target - num, counter.getAndIncrement());
        });
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i]) && i != map.get(nums[i])) {
                return new int[]{i, map.get(nums[i])};
            }
        }
        return new int[]{};
    }
}