class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        stack = []
        intervals.sort()

        for i in intervals:
            if not stack:
                stack.append(i)

            if stack[-1][-1] >= i[0]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])

            else:
                stack.append(i)

        return stack
        