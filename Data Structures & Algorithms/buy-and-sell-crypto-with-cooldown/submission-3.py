class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 4 for _ in range(n)]

        dp[0][0] = -prices[0]
        
        for i in range(1, n):
            for j in range(4):
                if j == 0:
                    dp[i][j] = max(dp[i - 1][0], dp[i - 1][1] - prices[i], dp[i - 1][3] - prices[i])
                if j == 1:
                    dp[i][j] = max(dp[i - 1][1], dp[i - 1][3])

                if j == 2:
                    dp[i][j] = dp[i-1][0] + prices[i]

                if j == 3:
                    dp[i][j] = dp[i-1][2]

        return max(map(max, dp))
        