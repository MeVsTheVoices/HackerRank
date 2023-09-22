package cs497.assignment2.removeduplicateletters;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
    public String removeDuplicateLetters(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }
        Map<Character, Integer> charCount = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            charCount.put(s.charAt(i), charCount.getOrDefault(s.charAt(i), 0) + 1);
        }

        List<Character> chars = new LinkedList<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            charCount.put(c, charCount.get(c) - 1);
            if (chars.contains(c)) {
                continue;
            }
            while (!chars.isEmpty() && chars.get(chars.size() - 1) > c && charCount.get(chars.get(chars.size() - 1)) > 0) {
                chars.remove(chars.size() - 1);
            }
            chars.add(c);
        }

        

        StringBuilder sb = new StringBuilder();
        for (Character c : chars) {
            sb.append(c);
        }
        return sb.toString();
    }
}