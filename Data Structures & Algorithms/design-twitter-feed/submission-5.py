class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follower = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if self.tweets[userId]:
            for ti, i in self.tweets[userId]:
                heapq.heappush(heap, (-ti, i))
                if len(heap) > 10:
                    heapq.heappop(heap)
        if self.follower[userId]:
            for p in self.follower[userId]:
                if p != userId:
                    for ti, id in self.tweets[p]:
                        heapq.heappush(heap, (-ti, id))
                        if len(heap) > 10:
                            heapq.heappop(heap)

        return [x[-1] for x in sorted(heap)[::-1]]
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
        
