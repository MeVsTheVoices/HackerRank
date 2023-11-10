# TwoSum
## Problem
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

## Intuition
uses the fact that for every x, there is only one target - x such that (target - x) + x == target

## Approach
My initial apporach was to use the naive exponential solution and iterate through the array twice, but I realized that I could use a hash table to store the values of the array as keys, and the index of the value as the value of the hash table. This way, I could iterate through the array once, and check if the hash table contains the target - x value, and if it does, I can return the index of the current value, and the index of the target - x value.
## Complexity
- Time complexity: O(n)
- Space complexity: O(n)

## Code
```java
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
```