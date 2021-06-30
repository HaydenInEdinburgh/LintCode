"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
# HARD

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.asc_nodes = []
        self.in_order(root)
        self.next_index = 0
    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return len(self.asc_nodes) > self.next_index
    """
    @return: return next node
    """
    def _next(self):
        # write your code here
        if not self.hasNext():
            return None

        next_num = self.asc_nodes[self.next_index]
        self.next_index += 1
        return next_num

    def in_order(self, root):
        if not root:
            return None

        self.in_order(root.left)
        self.asc_nodes.append(root)
        self.in_order(root.right)
