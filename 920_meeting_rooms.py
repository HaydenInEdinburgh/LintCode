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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals:
            return True

        events = []
        for inter in intervals:
            events.append((inter.start, 1))
            events.append((inter.end, -1))
        events.sort()

        status = 0
        for _, act in events:
            status += act
            if status > 1:
                return False

        return True