class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()


        while True:
            num = n
            total = 0

            if n in visited:
                return False
            visited.add(n)
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num = num // 10
            n = total

            if total == 1:
                return True

            
            


            
        