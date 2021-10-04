"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        m, n = len(list1), len(list2)
        if not m and not n:
            return []
        if not m:
            return list2
        if not n:
            return list1

        res = []
        i, j = 0, 0
        while i <m and j <n:
            int_a, int_b = list1[i], list2[j]
            if int_a.start < int_b.start:
                self.push_back(int_a, res)
                i += 1
            else:
                self.push_back(int_b, res)
                j += 1
        while i< m:
            self.push_back(list1[i], res)
            i += 1
        while j< n:
            self.push_back(list2[j], res)
            j += 1

        return res



    def push_back(self, interval, res):
        if not res:
            res.append(interval)
            return

        last_interval = res[-1]
        if last_interval.end < interval.start:
            res.append(interval)
            return

        last_interval.end = max(interval.end, last_interval.end)
