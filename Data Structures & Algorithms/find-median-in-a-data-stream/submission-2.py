class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        while self.right and -self.left[0] > self.right[0]:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        while len(self.left) > len(self.right) + 1:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)
        
        while len(self.right) > len(self.left) + 1:
            x = -heapq.heappop(self.right)
            heapq.heappush(self.left, x)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        
        else:
            return -self.left[0] if len(self.left) > len(self.right) else self.right[0]
        
        