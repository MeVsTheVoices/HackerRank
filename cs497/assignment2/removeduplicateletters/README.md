# Intuition
It's asking for linear time, I started off about to implement counting sort, but, decided against, by the time I had implemented a hashmap to save on space, I realized, that I already had a sorted keyset to work from. With that, I was able to implement a linear time solution. All this required was that I then iterate through the hash maps keyset and return the largest gap between two keys.

# Approach
Store everything in a hash map, then iterate through the keyset, and return the largest gap between two keys.

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```
class Solution {
    public int maximumGap(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int max = 0;
        for (int i = 0; i < nums.length; i++)
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);

        Iterator<Integer> it = map.keySet().iterator();
        int itPlusOne = it.next();

        HashMap<Integer, Integer> map2 = new HashMap<>();
        while (it.hasNext()) {
            int itNext = it.next();
            map2.put(itNext, itNext - itPlusOne);
            itPlusOne = itNext;
        }

        Iterator<Integer> it2 = map2.keySet().iterator();
        while (it2.hasNext()) {
            int itNext = it2.next();
            if (map2.get(itNext) > max)
                max = map2.get(itNext);
        }

        return max;

    }

}
```