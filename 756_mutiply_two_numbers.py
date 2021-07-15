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
    @param l1: the first list
    @param l2: the second list
    @return: the product list of l1 and l2
    """
    def multiplyLists(self, l1, l2):
        # write your code here
        if not l1 and not l2:
            return None

        l1_num = self.get_num(l1)
        l2_num = self.get_num(l2)

        res = l1_num * l2_num
        return res

    def get_num(self, node):
        res = 0
        while node:
            res = res*10 + node.val
            node = node.next
        return res