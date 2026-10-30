class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def can_flow_both(r, c):
            pac = atl = False
            visited = set()

            def dfs(i, j):
                nonlocal pac, atl
                if pac and atl:                 # 两个海都到了，提前结束
                    return
                visited.add((i, j))
                if i == 0 or j == 0:
                    pac = True                  # 碰到上边或左边，能流进太平洋
                if i == m - 1 or j == n - 1:
                    atl = True                  # 碰到下边或右边，能流进大西洋
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if (0 <= ni < m and 0 <= nj < n
                            and (ni, nj) not in visited
                            and heights[ni][nj] <= heights[i][j]):   # 往相等或更低处流
                        dfs(ni, nj)

            dfs(r, c)
            return pac and atl

        return [[i, j] for i in range(m) for j in range(n) if can_flow_both(i, j)]