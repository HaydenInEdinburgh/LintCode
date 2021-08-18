"""
Definition of Interval.

"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        if not intervals:
            return [newInterval]

        events = []
        intervals.append(newInterval)
        for inter in intervals:
            events.append((inter[0], 1))
            events.append((inter[1], -1))
        events.sort(key=lambda x: [x[0], -x[1]])
        print(events)

        stat = 0
        start, end = None, None
        res = []
        for time, act in events:
            stat += act
            if stat == 1 and start is None:
                start = time
            elif stat == 0 and start is not None:
                end = time
                res.append((start, end))
                start, end = None, None

        return res

if __name__ == '__main__':
    s = Solution()
    intervals = [(1,5)]
    n_interval = (0, 3)
    print(s.insert(intervals, n_interval))