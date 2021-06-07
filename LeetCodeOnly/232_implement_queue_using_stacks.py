class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_A = []
        self.stack_B = []
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_A.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_B:
            self.move()
        return self.stack_B.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_B:
            self.move()
        return self.stack_B[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_A) == 0 and len(self.stack_B) == 0

    def move(self):
        while self.stack_A:
            self.stack_B.append(self.stack_A.pop())
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()