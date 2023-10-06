package leetcode.threesum;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<HashMap<Integer, Integer>> triplets = new HashSet<HashMap<Integer, Integer>>();
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            for (int j = 0; j < nums.length; j++) {
                if (i == j)
                    continue;
                int y = nums[j];
                for (int k = 0; k < nums.length; k++) {
                    if (i == k || j == k)
                        continue;
                    int z = nums[k];
                    if (x + y + z == 0) {
                        HashMap<Integer, Integer> triplet = new HashMap<Integer, Integer>();
                        int[] list = { x, y, z };
                        for (int l = 0; l < list.length; l++) {
                            triplet.put(list[l], triplet.getOrDefault(list[l], 0) + 1);
                        }
                        triplets.add(triplet);
                    }
                }
            }
        }
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for (HashMap<Integer, Integer> triplet : triplets) {
            List<Integer> list = new ArrayList<Integer>();
            for (Map.Entry<Integer, Integer> entry : triplet.entrySet()) {
                for (int i = 0; i < entry.getValue(); i++)
                    list.add(entry.getKey());
            }
            result.add(list);
        }
        return result;
    }
}