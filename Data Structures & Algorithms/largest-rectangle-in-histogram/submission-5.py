class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = [0]

        max_area = 0

        for h in range(len(heights)):
            while len(stack) >= 2 and heights[stack[-1]] > heights[h]:
                mid = stack.pop()
                left = stack[-1]
                right = h

                curr_area = (right - left - 1) * heights[mid]
                max_area = max(curr_area, max_area)

            stack.append(h)

        return max_area
                


        