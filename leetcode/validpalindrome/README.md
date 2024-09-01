# Intuition
Given a string, we need to determine if it is a palindrome. A palindrome is a string that reads the same forwards and backwards. We can solve this problem by first converting the string to lowercase and then removing all non-alphanumeric characters. We can then compare the original string with the reversed string to determine if it is a palindrome.

# Approach
1. Convert the string to lowercase.
2. Remove all non-alphanumeric characters.
3. Reverse the string.
4. Compare the original string with the reversed string.

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```python3 []
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCased = s.lower()
        alphaOnly = [ x if x.isalpha() or x.isdigit() else "" for x in lowerCased]
        reversed = alphaOnly[::-1]
        return ''.join(alphaOnly) == ''.join(reversed)
```