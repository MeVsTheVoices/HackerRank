package cs497.midterm1.findlongestpalindrome;



class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 0) return "";
        if (s.length() == 1) return s;
        String longestSoFar = "";
        for (int i = 0; i < s.length(); i++) {
            String current = "";
            int left = i;
            int right = i;
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                current = s.substring(left, right + 1);
                left--;
                right++;
            }
            if (current.length() > longestSoFar.length()) longestSoFar = current;
            current = "";
            left = i;
            right = i + 1;
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                current = s.substring(left, right + 1);
                left--;
                right++;
            }
            if (current.length() > longestSoFar.length()) longestSoFar = current;
        }
        return longestSoFar;
    }
}