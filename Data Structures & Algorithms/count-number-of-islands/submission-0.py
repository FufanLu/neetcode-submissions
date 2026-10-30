class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == '0':
                return

            grid[i][j] = '0'

            for dx, dy in directions:
                new_i = dx + i
                new_j = dy + j

                dfs(new_i, new_j)

        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)


        return count



        