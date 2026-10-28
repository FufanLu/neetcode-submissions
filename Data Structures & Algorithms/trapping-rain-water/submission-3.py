class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0

        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                area += (left_max - height[left])
                left += 1

            else:
                right_max = max(height[right], right_max)
                area += (right_max - height[right])
                right -= 1


        return area


        