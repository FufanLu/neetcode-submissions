class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))


        if fresh_count == 0:
            return 0

        if not queue:
            return -1

        last_time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y, time = queue.popleft()
            last_time = max(time, last_time)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny <n and grid[nx][ny] == 1:
                    fresh_count -= 1
                    grid[nx][ny] = 2
                    queue.append((nx, ny, time + 1))

        return last_time if fresh_count == 0 else -1

