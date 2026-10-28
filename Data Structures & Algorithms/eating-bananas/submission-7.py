class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_count = float('inf')

        while left <= right:
            mid = (right - left) // 2 + left
            hour = 0
            for pile in piles:
               hour += ((pile + mid - 1)// mid)

            if hour <= h:
                min_count = min(mid, min_count)
                right = mid - 1
            
            else:
                left = mid + 1


        return min_count
