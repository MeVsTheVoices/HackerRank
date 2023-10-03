# Intuition
We take each string, then shorten it until it matches the start of every other string, if it's larger than the longest string we've found so far, we save that result and keep on going.

# Approach
If we have no strings, return "". Otherwise, take each string and shorten it from the end until it matches every other string. If the string we end up with is larger than the longest string we've found, we save that and carry on.

# Complexity
- Time complexity: O(n^2)

- Space complexity: O(1)


# Code
```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        String longest = "";
        for (int i = 0; i < strs.length; i++) {
            String s = strs[i];
            while (!isCommon(strs, s) && s.length() > 0) {
                s = s.substring(0, s.length() - 1);
            }
            if (s.length() > longest.length()) {
                longest = s;
            }
        }
        return longest;
    }

    private boolean isCommon(String[] strs, String s) {
        for (int i = 0; i < strs.length; i++) {
            if (!strs[i].startsWith(s)) {
                return false;
            }
        }
        return true;
    }
}
```