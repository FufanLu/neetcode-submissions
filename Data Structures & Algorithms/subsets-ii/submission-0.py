class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        path = []

        def backTracking(index):
            ans.append(path[:])

            if index == len(nums):
                return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                backTracking(i + 1)
                path.pop()

        backTracking(0)

        return ans


        