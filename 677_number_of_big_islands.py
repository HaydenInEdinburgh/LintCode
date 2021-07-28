class UnionFind:
    def __init__(self, n):
        self.father = {i:i for i in range(n)}
        self.size = [0] * n


    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_b] = root_a
            self.size[root_a] += self.size[root_b]
            self.size[root_b] = 0
    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node
class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """
    def numsofIsland(self, grid, k):
        # Write your code here
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m *n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uf.size[(i*n) + j] = 1


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    _i, _j = i+di, j+dj
                    if self.isValid(grid, _i, _j):
                        uf.union(i*n+j, _i*n+_j)

        cnt = 0
        for size in uf.size:
            if size >= k:
                cnt += 1

        return cnt

    def isValid(self, grid, i, j):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return False
        return grid[i][j]