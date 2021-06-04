import sys


class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        if not n:
            return 0

        graph = self.get_graph(roads, n)
        res = - sys.maxsize
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                unionSet = set.union(graph[a], graph[b])
                res = max(res, len(unionSet))

        return res

    def get_graph(self, roads, n):
        graph = {i: set() for i in range(n)}
        for a, b in roads:
            graph[a].add((a,b))
            graph[b].add((a,b))
        return graph
if __name__ == '__main__':
    s = Solution()
    n = 8
    roads =[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    print(s.get_graph(roads, n))
    print(s.maximalNetworkRank(n, roads))