package leetcode.validparentheses;

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        if (s.length() == 0) return true;
        Stack<Character> stack = new Stack<>();
        char[] letters = s.toCharArray();
        for (int i = 0; i < letters.length; i++) {
            if (letters[i] == '(' || letters[i] == '[' || letters[i] == '{')
                stack.push(letters[i]);
            else if (stack.isEmpty()) return false;
            else if (letters[i] == ')' && stack.pop() != '(') return false;
            else if (letters[i] == ']' && stack.pop() != '[') return false;
            else if (letters[i] == '}' && stack.pop() != '{') return false;
        }
        if (stack.isEmpty()) return true;
        else return false;
    }   
}