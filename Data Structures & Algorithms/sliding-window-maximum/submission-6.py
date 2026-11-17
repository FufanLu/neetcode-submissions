class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        ans = []

        for i in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)

            if queue and queue[0] < i - k +1:
                queue.popleft()

            if i - k + 1 >= 0:
                ans.append(nums[queue[0]])

        return ans
        