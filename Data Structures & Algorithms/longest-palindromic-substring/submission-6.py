class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = -1
        longst = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        if j - i + 1 > longst:
                            start = i
                            longst = j - i +1
                    else:
                        if dp[i + 1][j - 1]:
                            dp[i][j] = True
                            if j - i + 1 > longst:
                                start = i
                                longst = j - i +1

        return s[start : start + longst]
                    


        