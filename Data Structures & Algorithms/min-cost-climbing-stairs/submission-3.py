class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]

        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]


        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-2], dp[-1])


        