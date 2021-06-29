# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root: return None
        nodes = []
        self.inorder(root, nodes)#acs

        return self.to_balanced_BST(nodes)


    def inorder(self, node, nodes):
        if not node:
            return None
        self.inorder(node.left, nodes)
        nodes.append(node)
        self.inorder(node.right, nodes)

    def to_balanced_BST(self, nodes):
        if not nodes:
            return None

        mid = len(nodes) // 2
        root = nodes[mid]
        root.left = self.to_balanced_BST(nodes[:mid])
        root.right = self.to_balanced_BST(nodes[mid+1:])

        return root
