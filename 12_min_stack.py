import sys
class MinStack:

    def __init__(self):

    # do intialization if necessary
        self.stack = []
        self.min_stack = []
    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):

    # write your code here
        self.stack.append(number)
        if not self.min_stack:
            self.min_stack.append(number)
        else:
            self.min_stack.append(min(self.min_stack[-1], number))

    """
    @return: An integer
    """

    def pop(self):

    # write your code here
        res = self.stack.pop()
        self.min_stack.pop()
        return res

    """
    @return: An integer
    """

    def min(self):
# write your code here
        return self.min_stack[-1]