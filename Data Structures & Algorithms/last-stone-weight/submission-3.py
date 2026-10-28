class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            num1 = heapq.heappop(stones)
            num2 = heapq.heappop(stones)
            if num1 == num2:
                continue
            res = num1 - num2
            heapq.heappush(stones, res)

        return -stones[0] if stones else 0
            

        