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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if not head:
            return None

        dummy_less = ListNode(-1)#d -> None
        dummy_larger = ListNode(-1)#d -> None

        node, node_less, node_larger = head, dummy_less, dummy_larger

        while node:
            if node.val < x:
                node_less.next = ListNode(node.val)
                node_less = node_less.next
            else:
                node_larger.next = ListNode(node.val)
                node_larger = node_larger.next
            node = node.next

        node_less.next = dummy_larger.next

        return dummy_less.next