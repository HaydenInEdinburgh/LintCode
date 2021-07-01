"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
Try to use Divide Conquer
"""
from collections import deque
class Solution:
    """
    @param root: a binary tree.
    @return: return the minimun subtree contains all the key nodes.
    """
    def subtreeWithAllKeyNodes(self, root):
        # write your code here.
        if not root:
            return None

        # bfs get all the nodes with its depth
        queue = deque([root])
        depth_dict, child_parent = {}, {}
        cur_depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                depth_dict[node] = cur_depth
                if node.left:
                    queue.append(node.left)
                    child_parent[node.left] = node
                if node.right:
                    queue.append(node.right)
                    child_parent[node.right] = node
            cur_depth += 1
        # get the deepest nodes
        max_depth = max(depth_dict.values())
        leaf_nodes = [n for n, v in depth_dict.items() if v == max_depth]

        # find there common root
        if len(leaf_nodes) == 1:
            return leaf_nodes[0]

        parent = {child_parent[n] for n in leaf_nodes}
        while len(parent) > 1:
            tmp = [child_parent[n] for n in parent]
            parent = set(tmp)

        return list(parent)[0]