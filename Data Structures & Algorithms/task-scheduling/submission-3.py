class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [-x for x in Counter(tasks).values()]
        heapq.heapify(count)

        queue = deque()
        times = 0

        while queue or count:
            times += 1

            if count:
                c = heapq.heappop(count) + 1
                if c != 0:
                    queue.append((c, (times + n)))


            while queue and queue[0][1] <= times:
                c, t = queue.popleft()
                heapq.heappush(count, c)


        return times

        