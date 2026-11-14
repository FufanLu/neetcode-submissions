class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counter = Counter(nums)
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        for v, k in heap:
            ans.append(k)

        return ans
        
        