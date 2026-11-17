class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prev = float('inf')
        max_profit = 0

        for p in prices:
            prev = min(prev, p)
            max_profit = max(p - prev, max_profit)

        return max_profit
        