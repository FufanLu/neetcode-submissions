class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:\

        n = len(grid)
        heap = []

        visited = set()

        heap.append((grid[0][0], 0, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            t, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue

            visited.add((x, y))
            if x == n - 1 and y == n - 1:
                return t

            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    heapq.heappush(heap, (max(t, grid[nx][ny]), nx, ny))

        

        