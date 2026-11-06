"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ends = []

        intervals.sort(key=lambda x : x.start)

        for i in intervals:
            if ends and ends[0] <= i.start:
                heapq.heappop(ends)

            heapq.heappush(ends, i.end)

        return len(ends)
        