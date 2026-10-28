class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        path = []
        total = 0
        ans = []

        def backTracking(index):
            nonlocal total
            if total == target:
                ans.append(path[:])
                return

            if total > target or index == len(nums):
                return


            for i in range(index, len(nums)):
                total += nums[i]
                path.append(nums[i])
                backTracking(i)
                path.pop()
                total -= nums[i]

        backTracking(0)

        return ans



            
        

        