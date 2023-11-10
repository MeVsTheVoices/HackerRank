package leetcode.longestcommonprefix;

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