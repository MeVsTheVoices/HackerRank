class Solution:
    def findDivisible(self, n):
        r = range(1, n + 1)
        divisors = [3, 5, 7]
        sum = 0
        for i in r:
            remainders = [i % d for d in divisors]
            if 0 in remainders:
                sum += i
        return sum