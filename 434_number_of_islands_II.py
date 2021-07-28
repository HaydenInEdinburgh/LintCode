"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class UnionFind:
    def __init__(self):
        self.father = {}
        self.size = 0

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size -= 1

    def find(self, point):
        path = []
        while self.father[point] != point:
            path.append(point)
            point = self.father[point]

        for p in path:
            self.father[p] = point

        return point

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        # write your code here
        if not n or not m: return []

        islands = set()
        uf = UnionFind()
        res = []

        for p in operators:
            x, y = p.x, p.y
            if (x, y) in islands:
                res.append(uf.size)
                continue
            islands.add((x, y))
            uf.father[(x, y)] = (x, y)
            uf.size += 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in islands:
                    continue
                uf.union((x, y), (nx, ny))
            #print(islands)
            res.append(uf.size)
        return res


if __name__ == '__main__':
    s = Solution()
    n = 4
    m = 5
    oprs = [[1,1],[1,2],[1,3],[1,4]]