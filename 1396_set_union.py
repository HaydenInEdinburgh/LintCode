class UnionFind:

    def __init__(self, length):

        self.father = {i: i for i in range(length)}
        self.count = length

    def union(self, a, b):

        a_root = self.find(a)
        b_root = self.find(b)

        if a_root == b_root:
            return

        self.father[b_root] = a_root
        self.count -= 1

    def find(self, point):

        path = []

        while point != self.father[point]:
            path.append(point)

            point = self.father[point]

        for p in path:
            self.father[p] = point

        return point


class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        # Write your code here
        uf = UnionFind(len(sets))
        idx = {}
        for i in range(len(sets)):
            cur_set = sets[i]
            for j in range(len(sets[i])):
                cur_ele = cur_set[j]
                if cur_ele in idx:
                    uf.union(i, idx[cur_ele])
                else:
                    idx[cur_ele] = i

        return uf.count