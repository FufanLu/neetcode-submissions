class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        remove = 0

        intervals.sort(key=lambda x : x[-1])
        stack = []

        for i in intervals:

            if stack and stack[-1][-1] > i[0]:
                remove += 1

            else:
                stack.append(i)


        return remove
                
        