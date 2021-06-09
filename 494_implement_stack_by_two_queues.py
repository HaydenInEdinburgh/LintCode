import collections
class Stack:
    def __init__(self):
        self.queueA = collections.deque([])
        self.queueB = collections.deque([])
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.queueA.append(x)
    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while len(self.queueA) >1:
            self.queueB.append(self.queueA.popleft())
        res = self.queueA.popleft()
        self.queueA, self.queueB = self.queueB, self.queueA
        return res

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while len(self.queueA) > 1:
            self.queueB.append(self.queueA.popleft())
        res = self.queueA.popleft()
        self.queueB.append(res)
        self.queueA, self.queueB = self.queueB, self.queueA
        return res
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.queueA) == 0 and len(self.queueB) == 0