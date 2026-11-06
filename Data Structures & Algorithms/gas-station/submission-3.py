class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        profit_cost = [0] * n

        for i in range(n):
            profit_cost[i] = gas[i] - cost[i]

        if sum(profit_cost) < 0:
            return -1

        total = 0
        index = 0
        for i in range(n):
            if total + profit_cost[i] < 0:
                total = 0
                index = i + 1
                continue

            else:
                total += profit_cost[i]

        return index

        