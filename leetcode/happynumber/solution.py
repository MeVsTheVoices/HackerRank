class Solution:
    def isHappy(self, n: int) -> bool:
        haveSeen = set()
        sumSoFar = 0
        while self.sumOfSquares(n) not in haveSeen and self.sumOfSquares(n) != 1:
            haveSeen.add(self.sumOfSquares(n))
            n = self.sumOfSquares(n)
        return self.sumOfSquares(n) == 1

    def sumOfSquares(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += (n % 10) ** 2
            n //= 10
        return sum
