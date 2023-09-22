# Intuition
My intuition was a bit off for this at first, my initial approach was comparable, but, it needed changes. To begin with, I sorted the characters, then deleted one of every character, then, I went backwards through that list and deleted the characters of the original array until only none were remaining. This approach instead uses the same bones, but, instead of the complexity of traversing two arrays, we use the hash map that was built already, and then check whether there are characters greater than the one we want to keep that occur after each character.

# Approach
First we go through and get a count of every character. From this we then loop through the string provided. We only want to keep one of each element, but, we want to check if, having deleted this element, instead of another, we would move a larger element closer to the front of the array. We use linked lists for easy insertion and remove, then rebuild that as a string to return a proper value.

# Complexity
- Time complexity: O(n^2)

- Space complexity: O(n)

# Code
```
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
```