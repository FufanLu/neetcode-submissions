class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        price = [float('inf')] * n
        price[src] = 0

        for _ in range(k + 1):
            temp = price[:]
            for s, d, p in flights:
                if price[s] == float('inf'):
                    continue

                if price[s] + p < temp[d]:
                    temp[d] = price[s] + p

            price = temp


        return -1 if price[dst] == float('inf') else price[dst] 
        