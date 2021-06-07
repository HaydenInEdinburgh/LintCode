class MyQueue:

    def __init__(self):

    # do intialization if necessary
        self.stack_A = []
        self.stack_B = []
    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):

    # write your code here
        self.stack_A.append(element)
    """
    @return: An integer
    """

    def pop(self):

    # write your code here
        if not self.stack_B:
            self.move()
        return self.stack_B.pop()
    """
    @return: An integer
    """

    def top(self):
        if not self.stack_B:
            self.move()
        return self.stack_B[-1]
# write your code here

    def move(self):
        while self.stack_A:
            self.stack_B.append(self.stack_A.pop())