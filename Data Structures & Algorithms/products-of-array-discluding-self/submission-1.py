class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = [1] * len(nums)
        suffix_product = [1] * len(nums)

        for i in range(1, len(nums)):
            pre_product[i] = pre_product[i-1] * nums[i-1]


        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

        return [pre_product[i] * suffix_product[i] for i in range(len(nums))]  

        