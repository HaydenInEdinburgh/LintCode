import collections
class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.queue = [collections.deque(v1), collections.deque(v2)]
        self.old, self.new = 0, 1
    """
    @return: An integer
    """
    def _next(self):
        # write your code here
        if self.queue[0] and self.queue[1]:
            self.old, self.new = self.new, 1 - self.new
            return self.queue[self.new].popleft()
        if self.queue[0]:
            return self.queue[0].popleft()
        if self.queue[1]:
            return self.queue[1].popleft()

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return self.queue[0] or self.queue[1]

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result