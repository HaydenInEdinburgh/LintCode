"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param node: a list node in the list
    @param x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        if not node: #no node inside
            node = ListNode(x)
            node.next = node
            return node

        p = node
        prev = None
        while True:
            prev = p
            p = p.next
            if prev.val <= x <= p.val:
                break
            if prev.val > p.val and (x < p.val or x > prev.val):
                break
            if p is node:#all the same
                break

        newNode = ListNode(x)
        newNode.next = p
        prev.next = newNode

        return newNode
