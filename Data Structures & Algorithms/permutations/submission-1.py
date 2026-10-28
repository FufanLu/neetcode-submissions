class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)

        path = []
        ans = []

        def backTracking():
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backTracking()
                    visited[i] = False
                    path.pop()


        backTracking()

        return ans

        