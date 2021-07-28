class UnionFind:
    def __init__(self, n):
        self.father = {i: i for i in range(n)}
        self.size = n

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size -= 1



class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n-1:
            return False

        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)

        return uf.size == 1

