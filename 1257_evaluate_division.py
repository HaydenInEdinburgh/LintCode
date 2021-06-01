class Solution:
    """
    @param equations:
    @param values:
    @param queries:
    @return: return a double type array
    """
    def calcEquation(self, equations, values, queries):
        # write your code here
        if not equations or not values or not queries:
            return []

        results = [-1.0] * len(queries)
        graph = self.get_graph(equations, values)
        # print(graph)
        for i  in range(len(queries)):
            start, target = queries[i]
            if start not in graph or target not in graph:
                results.append(-1.0)
                continue
            res = self.dfs(start, target, 1, {start}, graph)
            results.append(res)
        return results

    def dfs(self, cur, target, res, path, graph):
        if cur == target:
            return res

        for next_node, value in graph[cur].items():
            if next_node in path:
                continue
            print(next_node, value)
            res *= value
            path.add(next_node)
            self.dfs(next_node, target, res, path, graph)
            path.remove(next_node)
            res /= value

        return -1.0

    def get_graph(self, equations, values):
        graph = {}
        for i, equa in enumerate(equations):
            #print(equa)
            a, b = equa[0], equa[1]
            self.build_link(graph, values[i], a, b)
        return graph

    def build_link(self, graph, value, a, b):
        # print(a, graph)
        if a not in graph:
            graph[a] = {}
            graph[a][a] = 1.0
        if b not in graph:
            graph[b] = {}
            graph[b][b] = 1.0
        graph[a][b] = value
        graph[b][a] = 1.0/ value

if __name__ == '__main__':
    s = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(s.calcEquation(equations, values, queries))


class Solution2:
    """
    @param equations:
    @param values:
    @param queries:
    @return: return a double type array
    """
    def calcEquation(self, equations, values, queries):
        # write your code here
        if not equations or not values or not queries:
            return []

        results = [-1.0] * len(queries)
        graph = self.get_graph(equations, values)
        # print(graph)
        for i  in range(len(queries)):
            start, target = queries[i]
            if start not in graph or target not in graph:
                continue
            self.dfs(start, target, 1.0, {start}, graph, i, results)
        return results

    def dfs(self, cur, target, res, path, graph, i, results):
        if cur == target:
            results[i] = res
            return

        for next_node, value in graph[cur].items():
            if next_node in path:
                continue
            res *= value
            path.add(next_node)
            self.dfs(next_node, target, res, path, graph, i, results)
            path.remove(next_node)
            res /= value

    def get_graph(self, equations, values):
        graph = {}
        for i, equa in enumerate(equations):
            #print(equa)
            a, b = equa[0], equa[1]
            self.build_link(graph, values[i], a, b)
        return graph

    def build_link(self, graph, value, a, b):
        # print(a, graph)
        if a not in graph:
            graph[a] = {}
            graph[a][a] = 1.0
        if b not in graph:
            graph[b] = {}
            graph[b][b] = 1.0
        graph[a][b] = value
        graph[b][a] = 1.0/ value
