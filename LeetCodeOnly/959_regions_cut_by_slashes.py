class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def regionsBySlashes(self, grid) -> int:
        n = len(grid)
        # divide one cell to 4 triangles
        uf = UnionFind(4 * n * n)
        for row in range(n):
            for col in range(n):
                cell = grid[row][col]
                index = 4 * (row * n  + col)
                if cell == ' ':
                    uf.union(index+0, index+1)
                    uf.union(index+1, index+2)
                    uf.union(index+2, index+3)
                if cell == '/':
                    uf.union(index+0, index+3)
                    uf.union(index+1, index+2)
                if cell == '\\':
                    uf.union(index+0, index+1)
                    uf.union(index+2, index+3)
                if row < n-1:
                    uf.union(index+2, (index + 4 * n) + 0)
                if col < n-1:
                    uf.union(index+1, (index + 4) + 3)

        res = 0
        for i in range(4 * n * n):
            if uf.find(i) == i:
                res += 1

        return res