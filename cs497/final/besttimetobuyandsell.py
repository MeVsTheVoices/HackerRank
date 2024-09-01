from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Use dynamic programming to solve this problem
        n = len(prices)
        if n == 0:
            return 0
        maximumProfit = [0] * n
        minimumPrice = prices[0]
        for i in range(1, n):
            maximumProfit[i] = max(maximumProfit[i-1], prices[i] - minimumPrice)
            minimumPrice = min(minimumPrice, prices[i])
        return maximumProfit[-1]