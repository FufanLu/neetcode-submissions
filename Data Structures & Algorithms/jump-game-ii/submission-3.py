class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 

        step = 0
        next_cover = 0
        curr_max = 0

        for index, num in enumerate(nums):
            next_cover = max(next_cover, index + num)
            if index == curr_max:
                step += 1
                curr_max = next_cover

            if curr_max >= len(nums) - 1:
                return step






        