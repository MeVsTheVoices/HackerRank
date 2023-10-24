package cs497.midterm1.validanagram;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        // If the strings are unequal in length, they can't be anagrams.
        if (s.length() != t.length()) return false;
        // We're going to use a map to keep track of the number of times each letter appears in s.
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        // We iterate through the elements of one of the strings and count the number of occurances
        // of each letter.
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // If we haven't seen the element before, we initialize for 0
            sMap.put(c, sMap.getOrDefault(c , 0) + 1);
        }
        // Now for the other string
        for (int i = 0; i < s.length(); i++) {
            char c = t.charAt(i);
            // If we haven't seen the element before, we initialize for 0
            tMap.put(c, tMap.getOrDefault(c , 0) + 1);
        }
        // Now we compare all elements of both maps
        for (char c : sMap.keySet()) {
            // If the number of occurances of a letter in s is not equal to the number of occurances
            // of that letter in t, then the strings are not anagrams.
            if (sMap.get(c) != tMap.getOrDefault(c, 0)) return false;
        }
        for (char c : tMap.keySet()) {
            // If the number of occurances of a letter in t is not equal to the number of occurances
            // of that letter in s, then the strings are not anagrams.
            if (tMap.get(c) != sMap.getOrDefault(c, 0)) return false;
        }
        // If we get here, then all the letters in s have the same number of occurances in t, so
        // the strings are anagrams.
        return true;
    }
}