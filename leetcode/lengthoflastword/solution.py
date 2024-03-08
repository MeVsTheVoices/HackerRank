class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        strs = s.split(" ")
        return len(strs[-1])