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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(-1)
        node = dummy
        l1_head, l2_head = l1, l2

        while l1_head and l2_head:
            if l1_head.val <= l2_head.val:
                node.next = l1_head
                l1_head = l1_head.next
            else:
                node.next = l2_head
                l2_head = l2_head.next
            node = node.next

        if l1_head:
            node.next = l1_head
        if l2_head:
            node.next = l2_head

        return dummy.next