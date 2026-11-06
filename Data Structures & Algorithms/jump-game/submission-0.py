class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0

        for index, num in enumerate(nums):
            if cover < index:
                return False

            cover = max(cover, num + index)

        return True
        