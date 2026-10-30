class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0

        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0

            if grid[x][y] == 0:
                return 0

            grid[x][y] = 0
            area = 1


            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                area += dfs(new_x, new_y)
            
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
            

        