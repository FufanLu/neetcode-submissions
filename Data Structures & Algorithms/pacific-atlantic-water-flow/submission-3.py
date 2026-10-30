class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        m = len(heights)
        n = len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, visited):
            visited.add((i , j))

            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited and heights[new_i][new_j] >= heights[i][j]:
                    dfs(new_i, new_j, visited)

        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n - 1, atl)
        
        for i in range(n):
            dfs(0, i, pac)
            dfs(m - 1, i, atl)

        ans = []

        for loc in atl:
            if loc in pac:
                ans.append([loc[0], loc[1]])

        return ans

