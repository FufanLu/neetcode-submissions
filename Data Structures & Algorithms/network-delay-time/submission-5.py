class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjacent_list = defaultdict(list)

        for u, v, t in times:
            adjacent_list[u].append((v, t))

        heap = [(0, k)]

        visited = set()
        res = 0
        while heap:
            time, start = heapq.heappop(heap)
            if start in visited:
                continue

            visited.add(start)
            res = time

            for v, t in adjacent_list[start]:
                if v in visited:
                    continue
                heapq.heappush(heap,(time + t, v))

        return res if len(visited) == n else -1



        