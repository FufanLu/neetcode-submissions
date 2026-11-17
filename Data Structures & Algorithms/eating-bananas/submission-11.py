class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        min_eat = float('inf')

        while left <= right:

            mid = (right - left) // 2 + left

            hour = 0
            for p in piles:
                if p % mid != 0:
                    hour += (p // mid) + 1
                else:
                    hour += (p // mid)

            if hour <= h:
                min_eat = min(min_eat, mid)
                right = mid -1
            
            else:
                left = mid + 1

        return min_eat

            
        