# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        nodes = self.get_nodes(root)
        visited = set()
        n = len(nodes)
        res = []
        for i in range(n-1):
            for j in range(i+1, n):
                if not self.isSame(nodes[i], nodes[j]):
                    continue
                if nodes[i] not in visited and nodes[j] not in visited:
                    res.append(nodes[i])
                visited.update({nodes[i], nodes[j]})

        return res

    def isSame(self, node_i, node_j):
        if not node_i and not node_j:
            return True
        if not node_i or not node_j:
            return False
        if node_j.val != node_i.val:
            return False

        same_l = self.isSame(node_i.left, node_j.left)
        same_r = self.isSame(node_i.right, node_j.right)

        return same_l and same_r

    def get_nodes(self, root):
        if not root:
            return []

        return self.get_nodes(root.left) + self.get_nodes(root.right) + [root]