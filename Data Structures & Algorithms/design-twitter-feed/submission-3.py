
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        users= self.following[userId] | {userId}
        
        for user in users:
            if user in self.tweets and self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweet_id = self.tweets[user][index]
                heapq.heappush(min_heap, (-time, tweet_id, user, index))
        
        while min_heap and len(res) < 10:
            neg_time, tweet_id, user, index = heapq.heappop(min_heap)
            res.append(tweet_id)
            
            if index > 0:
                prev_index = index - 1
                prev_time, prev_tweet_id = self.tweets[user][prev_index]
                heapq.heappush(min_heap, (-prev_time, prev_tweet_id, user, prev_index))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)