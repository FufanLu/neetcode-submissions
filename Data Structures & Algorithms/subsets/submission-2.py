class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []

        def backTracking(index):
            ans.append(path[:])

            if index == len(nums):
                return


            for i in range(index, len(nums)):
                path.append(nums[i])
                backTracking(i + 1)
                path.pop()

        backTracking(0)

        return ans

        