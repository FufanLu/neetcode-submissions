class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        path = []
        ans = []
        left = 0
        right = 0

        def backTracking():
            nonlocal left, right
            if len(path) == 2 * n:
                ans.append(''.join(path[:]))
                return

            if left < n:
                path.append('(')
                left += 1
                backTracking()
                left -= 1
                path.pop()

            if right < left:
                path.append(')')
                right += 1
                backTracking()
                right -= 1
                path.pop()

        backTracking()

        return ans

        