class CircularQueue:
    def __init__(self, n):
        # do intialization if necessary
        self.maxLen = n
        self.queue = []
    """
    @return:  return true if the array is full
    """
    def isFull(self):
        # write your code here
        return len(self.queue) >= self.maxLen
    """
    @return: return true if there is no element in the array
    """
    def isEmpty(self):
        # write your code here
        return len(self.queue) == 0
    """
    @param element: the element given to be added
    @return: nothing
    """
    def enqueue(self, element):
        # write your code here
        if self.isFull():
           return
        self.queue.append(element)
    """
    @return: pop an element from the queue
    """
    def dequeue(self):
        # write your code here
        if self.isEmpty():
            return
        return self.queue.pop(0)
