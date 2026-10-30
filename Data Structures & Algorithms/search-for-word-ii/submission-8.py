class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = w


        ans = []
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backTracking(i, j, parent):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if board[i][j] not in parent.children:
                return

            if visited[i][j]:
                return

            visited[i][j] = True

            c = board[i][j]
            if parent.children[c].word:
                ans.append(parent.children[c].word)
                parent.children[c].word = None

            for dx, dy in directions:
                new_i = i + dx
                new_j = j + dy
                backTracking(new_i, new_j, parent.children[c])
            
            visited[i][j] = False

            if not parent.children[c] and not parent.children[c].word:
                del parent.children[c]


        
        for i in range(m):
            for j in range(n):
                backTracking(i, j, root)

        return ans