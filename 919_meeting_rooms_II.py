"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0

        events = []
        for i in intervals:
            events.append((i.start, 1))
            events.append((i.end, -1))
        events = sorted(events, key= lambda e: [e[0], -e[1]])

        cur, maximum = 0, 0
        for _, act in events:
            cur += act
            maximum = max(maximum, cur)

        return maximum
