class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        total = 0
        n = len(digits)
        digits = digits[::-1]

        for i in range(n):
            total += digits[i] * (10 ** i)
        total += 1
        ans = []
        while total > 0:
            d = total % 10
            ans.append(d)
            total = total // 10

        return ans[::-1]



        

        