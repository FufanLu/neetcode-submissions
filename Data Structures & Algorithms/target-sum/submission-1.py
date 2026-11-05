class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        if abs(target) > total or (total + target) % 2 == 1:
            return 0


        nt = (target + total) // 2
        dp = [0] * (nt + 1)
        dp[0] = 1

        for n in nums:
            for j in range(nt, n - 1, -1):
                dp[j] += dp[j - n]

        return dp[nt] 
        