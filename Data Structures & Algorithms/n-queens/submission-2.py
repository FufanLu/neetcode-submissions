class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]

        def isValid(x, y):
            for i in range(n):
                if board[i][y] == 'Q':
                    return False

            dx = x - 1
            dy = y - 1
            while dx >= 0 and dy >=0:
                if board[dx][dy] == 'Q':
                    return False
                dx -= 1
                dy -= 1

            dx = x - 1
            dy = y + 1
            while dx >= 0 and dy < n:
                if board[dx][dy] == 'Q':
                    return False
                dx -= 1
                dy += 1

            return True


        ans = []

        def backTracking(m):
            if m == n:
                ans.append([''.join(board[i]) for i in range(n)])
                return

            for i in range(n):
                if isValid(m, i):
                    board[m][i] = 'Q'
                    backTracking(m + 1)
                    board[m][i] = '.'

        backTracking(0)

        return ans
                    



        