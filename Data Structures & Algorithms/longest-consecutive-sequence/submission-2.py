class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longst = 0
        nums = set(nums)
        for num in nums:
            if num - 1 in nums:
                continue
            
            curr = 0
            i = num
            while i in nums:
                curr += 1
                i += 1

            longst = max(longst, curr)

        return longst

            
        