class User:
    def __init__(self, id):
        self.id = id
        self.tweets = []
        self.feed = []
        self.following = set()

def merge_k_sorted_lists(lists):
    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    result = []
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)

        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))
            
    return result

class Twitter:
    def __init__(self):
        self.users = {}
        self.timestamp = 0
    
    def verifyUser(self, id_):
        if id_ not in self.users:
            self.users[id_] = User(id_)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.verifyUser(userId)
        
        curUser = self.users[userId]
        curUser.tweets.append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.verifyUser(userId)
        curUser = self.users[userId]

        lists = []

        if curUser.tweets:
            lists.append(curUser.tweets[::-1][:10])
            
        for followeeId in curUser.following:
            self.verifyUser(followeeId)
            if self.users[followeeId].tweets:
                lists.append(self.users[followeeId].tweets[::-1][:10])
        
        merged_tuples = merge_k_sorted_lists(lists)
        return [tweetId for time, tweetId in merged_tuples[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.verifyUser(followerId)
        self.verifyUser(followeeId)

        self.users[followerId].following.add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.verifyUser(followerId)
        self.verifyUser(followeeId)

        self.users[followerId].following.discard(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
