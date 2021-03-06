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
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        # write your code here
        if not n or not head:
            return

        idx = 0
        node = head
        while node:
            node = node.next
            idx += 1

        target_idx = idx - n
        node = head
        idx = 0
        while node:
            if idx == target_idx:
                return node
            node = node.next
            idx += 1

        return None