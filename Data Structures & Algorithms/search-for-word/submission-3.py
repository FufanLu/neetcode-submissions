class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backTracking(i, j, index):
            if index == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False

            if visited[i][j]:
                return False

            visited[i][j] = True
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if backTracking(new_i, new_j, index + 1):
                    return True

            visited[i][j] = False   


        for i in range(m):
            for j in range(n):
                if backTracking(i, j, 0):
                    return True
        
        return False


            