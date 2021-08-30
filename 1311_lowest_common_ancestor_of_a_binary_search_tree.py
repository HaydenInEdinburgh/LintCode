"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        if not root:
            return None
        if p == q:
            return p

        if p.val > q.val:# make sure p <= q
            p, q = q, p

        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val <= root.val <= q.val:
            return root
