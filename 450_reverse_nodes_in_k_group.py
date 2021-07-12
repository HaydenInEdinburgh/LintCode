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
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if not head:
            return
        dummy = ListNode(-1, head)
        prev = dummy
        while prev:
            prev = self.reverse_next_k(prev, k)

        return dummy.next

    def find_kth_node(self, head, k):
        cnt = 0
        node = head
        while node.next and cnt < k:
            cnt += 1
            node = node.next

        if cnt < k:
            return None
        return node

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        return prev

    def reverse_next_k(self, head, k):
        # head -> n1 -> n2 -> ... -> nk -> nk+1
        # to head -> nk -> nk-1 -> ... -> n1 -> nk+1
        n1 = head.next
        nk = self.find_kth_node(head, k)
        if not nk:
            return None
        nk_plus = nk.next
        # reverse k nodes
        nk.next = None #
        nk = self.reverse(n1)
        head.next = nk
        n1.next = nk_plus

        return n1