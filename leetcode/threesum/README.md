# Intuition
My original intuition exceeding time limits, so I changed a few things.

# Approach
We create a map so we can keep track of whether an element exists. Then for two increasing pointers, see whether the map contains the third value that summed with the first two, would return the correct result.

# Complexity
- Time complexity: O(n^2)

- Space complexity: O(n)

# Code
```
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        Set<List<Integer>> set = new HashSet<>();
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int j = 0; j < nums.length; j++) {
            for (int k = j + 1; k < nums.length; k++) {
                int target = 0 - nums[j] - nums[k];
                if (map.containsKey(target) && map.get(target) != j && map.get(target) != k) {
                    List<Integer> list = new ArrayList<>();
                    list.add(nums[j]);
                    list.add(nums[k]);
                    list.add(target);
                    list.sort(null);
                    set.add(list);
                }
            }
        }
        result.addAll(set);
        return result;
    }
}

```