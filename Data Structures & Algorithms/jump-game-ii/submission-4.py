class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 

        curr = 0
        next = 0
        step = 0

        for index, num in enumerate(nums):
            next = max(next, index + num)
            if index == curr:
                curr = next
                step += 1

            if curr >= len(nums) - 1:
                break

        return step



        