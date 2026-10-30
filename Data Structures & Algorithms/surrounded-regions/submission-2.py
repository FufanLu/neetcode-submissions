import sys
sys.setrecursionlimit(10 ** 6)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if board[i][j] == 'X':
                return

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            board[i][j] = 'T'

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                    dfs(ni, nj)
            

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if board[i][j] == 'O':
                        dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

                

        