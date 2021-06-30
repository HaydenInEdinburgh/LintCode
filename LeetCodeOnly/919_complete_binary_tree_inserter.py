# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.nodes = deque([]) # nodes without child
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            else:
                self.nodes.append(node)


    def insert(self, v: int) -> int:
        node = self.nodes[0]
        parent_val = node.val

        if not node.left:
            node.left = TreeNode(v)
            self.nodes.append(node.left)
        else:
            node.right = TreeNode(v)
            self.nodes.append(node.right)
            self.nodes.popleft()

        return parent_val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()