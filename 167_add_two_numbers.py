"""
Definition of ListNode

"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        # write your code here
        if not l1 and not l2:
            return None

        carry = 0
        node_1, node_2 = l1, l2
        dummy = ListNode(-1, None)
        prev = dummy
        while node_1 or node_2 or carry:
            n_1 = node_1.val if node_1 else 0
            n_2 = node_2.val if node_2 else 0
            node_sum = n_1 + n_2 + carry
            final = node_sum % 10
            carry = node_sum //10
            prev.next = ListNode(final, None)
            prev = prev.next
            node_1 = node_1.next if node_1 else None
            node_2 = node_2.next if node_2 else None


        return dummy.next