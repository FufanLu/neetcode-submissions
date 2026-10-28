class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []

        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1


        for i in num_dict.keys():
            heapq.heappush(heap, (num_dict[i], i))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for i in range(k):
            ans.append(heap[i][-1])

        return ans

        



        