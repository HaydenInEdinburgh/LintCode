"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if not head or not n:
            return

        prev_map = {}
        node = head
        while node.next:
            prev_map[node.next] = node
            node = node.next

        for _ in range(n-1):
            node = prev_map[node]

        if node in prev_map:
            prev_map[node].next = node.next
        else:
            head = head.next

        return head