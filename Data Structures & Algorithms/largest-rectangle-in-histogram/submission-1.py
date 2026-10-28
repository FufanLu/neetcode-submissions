class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        heights = [0] + heights

        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while len(stack) >= 2 and heights[stack[-1]] > h:
                mid = stack.pop()
                left = stack[-1]
                right = i
                max_area = max(max_area, heights[mid] * (right - left - 1))
            stack.append(i)

        return max_area




        