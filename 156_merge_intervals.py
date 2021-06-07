"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """

    def merge(self, intervals):
        # write your code here
        if not intervals:
            return []

        ongoing = 0
        timestamps = []
        results = []

        for i in intervals:
            timestamps.append((i.start, 1))
            timestamps.append((i.end, -1))

        timestamps.sort(key = lambda x: (x[0], -x[1]))
        print(timestamps)
        tmp = Interval()
        for time, act in timestamps:
            if ongoing == 0:
                tmp.start = time

            ongoing += act
            if ongoing == 0:
                tmp.end = time
                results.append(tmp)
                tmp = Interval()

        return results


if __name__ == '__main__':
    s = Solution()
    intervals = [(2, 3), (2, 2), (3, 3), (1, 3), (5, 7), (2, 2), (4, 6)]
    intervals = [Interval(s, e) for s, e in intervals]
    results = s.merge(intervals)
    print([(r.start, r.end) for r in results])
