class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(word):
            return word == word[::-1]


        path = []
        ans = []

        def backTracking(index):
            if index == len(s):
                ans.append(path[:])
                return

            for i in range(index, len(s)):
                sub_str = s[index : i + 1]
                if isPalindrome(sub_str):
                    path.append(sub_str)
                    backTracking(i + 1)
                    path.pop()


        backTracking(0)

        return ans
        