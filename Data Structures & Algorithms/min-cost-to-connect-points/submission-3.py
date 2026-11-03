class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        heap = [(0, 0)]

        ans = 0
        visited = set()

        while len(visited) < len(points):
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue

            visited.add(i)
            ans += cost

            for j in range(len(points)):
                if j not in visited:
                    x1, x2 = points[i][0], points[j][0]
                    y1, y2 = points[i][1], points[j][1]
                    heapq.heappush(heap, ((abs(x1 - x2) + abs(y1 - y2)), j))

        return ans

        