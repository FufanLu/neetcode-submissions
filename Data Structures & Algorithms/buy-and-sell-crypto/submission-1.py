class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min = float('inf')
        
        max_income = 0

        for price in prices:
            prev_min = min(prev_min, price)
            max_income = max((price - prev_min), max_income)

        return max_income
