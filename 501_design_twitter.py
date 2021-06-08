'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
import heapq


class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
        print(user_id, tweet_text)
        return tweet_text
class MiniTwitter:

    def __init__(self):
        self.timestamp_id = 0
        self.follow_map = {} # userId to following set
        self.post_map = {} # userId to user's posts
    # do intialization if necessary

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """

    def postTweet(self, user_id, tweet_text):
    # write your code here
        self.timestamp_id += 1
        tweet = Tweet.create(user_id, tweet_text)
        if user_id in self.post_map:
            self.post_map[user_id].append((self.timestamp_id, tweet))
        else:
            self.post_map[user_id] = [(self.timestamp_id, tweet)]

        return tweet
    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """

    def getNewsFeed(self, user_id):
        # write your code here
        rt = []
        if user_id in self.post_map:
            rt = self.post_map[user_id][-10:]

        if user_id in self.follow_map:
            for friend in self.follow_map[user_id]:
                if friend in self.post_map:
                    rt.extend(self.post_map[friend][-10:])
        rt.sort(key= lambda x: x[0])
        return [tweet for time, tweet in rt[-10:][::-1]]
    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """

    def getTimeline(self, user_id):
        # write your code here
        if user_id not in self.post_map:
            return []
        return [tweet for time, tweet in self.post_map[user_id][-10:][::-1]]

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def follow(self, from_user_id, to_user_id):

    # write your code here
        if from_user_id not in self.follow_map:
            self.follow_map[from_user_id] = set()
        self.follow_map[from_user_id].add(to_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id not in self.follow_map:
            return
        self.follow_map[from_user_id].remove(to_user_id)