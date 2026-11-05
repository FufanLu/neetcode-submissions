class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        total = 0

        for num in nums:
            if total + num > num:
                total += num
            else:
                total = num
            
            max_sum = max(max_sum, total)


        return max_sum