class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []

        nums.sort()

        if nums[0] > 0:
            return []

        ans = []
        
        n = len(nums)
        for i in range(n):
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -=1 

        return ans

                




