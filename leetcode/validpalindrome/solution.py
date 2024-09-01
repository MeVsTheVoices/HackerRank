class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCased = s.lower()
        alphaOnly = [ x if x.isalpha() or x.isdigit() else "" for x in lowerCased]
        reversed = alphaOnly[::-1]
        return ''.join(alphaOnly) == ''.join(reversed)