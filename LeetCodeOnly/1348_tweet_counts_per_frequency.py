import heapq
class TweetCounts:

    def __init__(self):
        self.tw_map = {} # {tweetName: heap}
        self.intervalMap = {'minute': 60, 'hour': 3600, 'day': 86400}
    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tw_map:
            self.tw_map[tweetName] = []
        self.tw_map[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int):
        if tweetName not in self.tw_map:
            return []
        interval = self.intervalMap[freq]
        size = (endTime - startTime)//interval +1

        res = [0] * size
        for i in self.tw_map[tweetName]:
            if (startTime <= i <= endTime):
                index = (i-startTime)//interval
                res[index] += 1

        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
if __name__ == '__main__':
    tweetCounts = TweetCounts()
    tweetCounts.recordTweet("tweet3", 0)
    tweetCounts.recordTweet("tweet3", 60)
    tweetCounts.recordTweet("tweet3", 10)
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))
    tweetCounts.recordTweet("tweet3", 120)
    print(tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))