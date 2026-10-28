class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        longst = 0

        for num in nums:
            if num - 1 in hashset:
                continue
            curr = 0
            while num in hashset:
                curr += 1
                longst = max(longst, curr)
                num += 1

        return longst
        