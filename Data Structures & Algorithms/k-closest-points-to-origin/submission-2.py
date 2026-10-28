class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for p in points:
            length = (p[0] ** 2 + p[1] ** 2) ** 0.5
            heapq.heappush(heap, (-length, p[0], p[1]))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for a in heap:
            ans.append([a[1], a[2]])

        return ans

        