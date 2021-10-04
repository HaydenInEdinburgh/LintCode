class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.stack = []
    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        # write your code here
        self.stack.append(val)
        if len(self.stack) > self.size:
            self.stack.pop(0)
        return sum(self.stack)/len(self.stack)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)