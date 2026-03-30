class Twitter:

    def __init__(self):

        self.newsFeed = []

        self.users = {}

        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.users:

            self.users[userId] = {userId}


        heapq.heappush(self.newsFeed, (-self.order, userId, tweetId))

        self.order += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        ret = []

        retNewsFeed = self.newsFeed.copy()

        postsReturned = 0

        while retNewsFeed and postsReturned < 10:

            post = heapq.heappop(retNewsFeed)

            if post[1] in self.users[userId]:

                ret.append(post[2])

                postsReturned += 1

        return ret


    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.users:

            self.users[followerId].add(followeeId)

        else:

            self.users[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId == followeeId:
            
            return

        if followerId in self.users:

            self.users[followerId].discard(followeeId)
        
