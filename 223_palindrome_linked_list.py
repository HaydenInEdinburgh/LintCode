"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    # Optimal Solution is use flasSlow pointer to find middle, reverse the [middle.next - tail], and compare one by one
    def isPalindrome(self, head):
        # write your code here
        if not head:
            return True

        n, prev_map = self.get_length(head)
        if n % 2 == 0:
            l, r = n//2, n//2+1
        else:
            l, r = n//2, n//2+2

        l_node, r_node = self.find_ith(head, l, n), self.find_ith(head, r, n)
        while l>0 and r<n+1:
            if l_node.val != r_node.val:
                return False
            l_node = prev_map.get(l_node, None)
            l -= 1
            r_node = r_node.next
            r += 1

        return True

    def find_ith(self, head, index, n):
        if index < 1 or index > n:
            return None
        node = head
        for _ in range(index-1):
            node = node.next
        return node

    def get_length(self, head):
        n = 0
        prev_map = {}
        while head:
            n += 1
            tmp = head
            head = head.next
            if head:
                prev_map[head] = tmp

        return n, prev_map