class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for index, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], index]

            num_dict[num] = index

        

