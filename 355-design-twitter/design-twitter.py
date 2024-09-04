class Twitter:
    class user:
        def __init__(self, userID):
            self.userID = userID
            self.followers = set([userID])
            self.following = set([userID])
        

    class tweet:
        def __init__(self, userID, tweetID):
            self.userID = userID
            self.tweetID = tweetID

    def __init__(self):
        # there's no function to create a user, so we should initialize them all from the get-go
        self.mapping = {} # maps a userID to a user struct with a set of followers and following
        for i in range(1, 501):
            self.mapping[i] = self.user(i)
        # can't delete tweets, so no point in keeping a linked list or that kind of data structure
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        t = self.tweet(userId, tweetId)
        # can't delete tweets, so keep a master DB of all tweets and append to that, so that it remains in order of time posted
        self.tweets.append(t)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # for that user's set of followers, retrieve the at most 10 recent tweets
        followers = self.mapping[userId].following
        count = 0
        feed = []
        # we need to get most recent 10
        for tweet in reversed(self.tweets):
            if tweet.userID in followers:
                feed.append(tweet.tweetID)
                count += 1
                if count >= 10:
                    break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # can't follow yourself
        if followerId != followeeId:
            # append to follower's following[]
            self.mapping[followerId].following.add(followeeId)
            # append to followee's followers[]
            self.mapping[followeeId].followers.add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # can't unfollow yourself
        if followerId != followeeId:
            # delete from follower's following[]
            self.mapping[followerId].following.discard(followeeId)
            # delete from followee's followers[]
            self.mapping[followeeId].followers.discard(followerId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)