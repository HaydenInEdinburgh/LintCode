class Solution:
    """
    @param graph: a 2D array
    @return: all possible paths from node 0 to node N-1
    """
    def allPathsSourceTarget(self, graph):
        # Write your code here
        if not graph:
            return []

        res = []
        visited = set()
        self.dfs(graph, 0, [0], res)
        return res

    def dfs(self, graph, curNode, path, res):
        if curNode == len(graph)-1:
            res.append(path[:])
            return

        for next in graph[curNode]:
            path.append(next)
            self.dfs(graph, next, path, res)
            path.pop()

if __name__ == '__main__':
    s = Solution()
    input = [[1,2],[3],[3],[]]
    print(s.allPathsSourceTarget(input))