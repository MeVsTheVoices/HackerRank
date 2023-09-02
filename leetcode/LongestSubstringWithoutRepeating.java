package leetcode;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;
        Set<Character> set = new HashSet<>();
        char[] letters = s.toCharArray();
        int max = 0;
        for (int i = 0; i < letters.length; i++) {
            int current = 0;
            while((i + current) < letters.length && set.add(letters[i + current]))
                current++;
            max = Math.max(max, current);
            set.clear();
        }
        return max;
    }
}