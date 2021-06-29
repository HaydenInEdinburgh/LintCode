class Solution:
    """
    @param root: the root node
    @param L: an integer
    @param R: an integer
    @return: the sum
    """
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0
        self.ans = 0
        self.dfs(root, L, R)
        return self.ans

    def dfs(self, root, L, R):
        if not root:
            return

        if L <= root.val <= R:
            self.ans += root.val
            self.dfs(root.left, L, R)
            self.dfs(root.right, L, R)

        if root.val < L:
            self.dfs(root.right, L, R)

        if root.val > R:
            self.dfs(root.left, L, R)