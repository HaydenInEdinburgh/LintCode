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

import heapq

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None

        dummy = ListNode(-1)
        queue = []
        self.id = 0
        for node in lists:
            if not node:
                continue
            self.push_node(queue, node)

        head = dummy
        while queue:
            _, _, node = heapq.heappop(queue)
            head.next = node
            head = head.next
            if not node.next:
                continue
            self.push_node(queue, node.next)

        return dummy.next

    def push_node(self, queue, node):
        self.id += 1
        heapq.heappush(queue, (node.val, self.id, node))