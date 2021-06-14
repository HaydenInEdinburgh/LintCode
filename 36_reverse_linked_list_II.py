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
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head or m >= n:
            return head
        dummy = ListNode(-1, head)
        mth_prev = self.find_kth(dummy, m-1)
        mth = mth_prev.next
        nth = self.find_kth(dummy, n)
        nth_next = nth.next
        nth.next = None

        new_head = self.reverse(mth)
        mth_prev.next = nth
        mth.next = nth_next

        return dummy.next

    def find_kth(self, head, k):
        for i in range(k):
            if head is None:
                return None
            head = head.next
        return head

    def reverse(self, curr):
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev