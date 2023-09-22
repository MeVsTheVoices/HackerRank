package cs497.assignment2.maximumgap;

import java.util.HashMap;
import java.util.Iterator;

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