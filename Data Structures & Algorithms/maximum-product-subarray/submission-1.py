class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_dp = [0] * n
        max_dp = [0] * n
        min_dp[0] = nums[0]
        max_dp[0] = nums[0]

        for i in range(1, n):
            candidates = (nums[i], min_dp[i - 1] * nums[i], max_dp[i - 1] * nums[i])

            min_dp[i] = min(candidates)
            max_dp[i] = max(candidates)

        return max(max_dp)


        
        