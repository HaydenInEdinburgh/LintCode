"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class NestedIterator(object):

    def __init__(self, nestedList):

    # Initialize your data structure here.
        self.next_element = None
        self.stack = []
        for element in reversed(nestedList):
            self.stack.append(element)

    # @return {int} the next element in the iteration
    def next(self):
    # Write your code here
        if self.next_element is None: # Cannot use if not self.next_element because of value can be 0
            self.hasNext()
        tmp, self.next_element = self.next_element, None
        return tmp

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        if self.next_element:
            return True
        while self.stack:
            top = self.stack.pop()
            if top.isInteger():
                self.next_element = top.getInteger()
                return True
            for ele in reversed(top.getList()):
                self.stack.append(ele)

        return False
# Write your code here


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())