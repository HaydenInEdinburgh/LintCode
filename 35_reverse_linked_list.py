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


class Solution1:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head:
            return None

        node_to_prev = {head: None}
        tail = head
        while tail.next is not None:
            node_to_prev[tail.next] = tail
            tail = tail.next

        dummy = ListNode(-1, tail)
        node = tail
        while node in node_to_prev:
            node.next = node_to_prev[node]
            node = node_to_prev[node]

        return dummy.next

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head or not head.next:
            return head

        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return curr