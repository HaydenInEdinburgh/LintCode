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
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head:
            return None

        dummy = ListNode(-1, head)
        visited = set()

        #find the last
        tail = head
        prev_map = {}
        while tail.next:
            prev_map[tail.next] = tail
            tail = tail.next

        node = head
        while node not in visited or tail not in visited:
            if node == tail or node.next == tail:
                return
            next = self.move_forward(node, tail, prev_map)
            visited.add(node)
            visited.add(tail)
            node = next
            tail = prev_map[tail]

    def move_forward(self, node, tail, prev_map):
        ori_next = node.next
        node.next = tail
        tail.next = ori_next
        prev_map[tail].next = None
        return tail.next