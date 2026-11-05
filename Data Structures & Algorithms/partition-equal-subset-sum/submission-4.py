class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, -1, -1):
                if j - num >= 0:
                    dp[j] = dp[j - num] or dp[j]

                    if dp[target]:
                        return True 

        return False
                
                

        
        