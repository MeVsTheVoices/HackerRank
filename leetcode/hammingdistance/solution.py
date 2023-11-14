class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distanceSoFar = 0
        while x or y:
            lowestBitOfX = x % 2
            lowestBitOfY = y % 2
            if lowestBitOfX ^ lowestBitOfY:
                distanceSoFar += 1
            x >>= 1
            y >>= 1
        return distanceSoFar