class UnionFind:
    def __init__(self, n):
        self.parent = {}
        for i in range(1, n+1):
            self.parent[i] = i

    def find(self, node):
        path = []
        while self.parent[node] != node:
            node = self.parent[node]
            path.append(node)
        for n in path:
            self.parent[n] = node
        return node

    def query(self, a, b):
        return self.find(a) == self.find(b)
    def connect(self, a, b):
        self.parent[self.find(a)] = self.find(b)


class Solution:
    """
    @param edges: List[List[int]]
    @return: List[int]
    """
    def findRedundantConnection(self, edges):
        # write your code here
        if not edges:
            return []

        uf = UnionFind(len(edges))
        for start, end in edges:
            if not uf.query(start, end):
                uf.connect(start, end)
            else:
                return [start, end]

        return None


if __name__ == '__main__':
    s = Solution()
    input = [[1,2],[1,3],[2,3]]
    print(s.findRedundantConnection(input))