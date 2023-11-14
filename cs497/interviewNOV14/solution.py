class Solution:
    def findDivisible(self, n):
        r = range(1, n + 1)
        c = 0
        for i in r:
            if (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
                c += i
        return c