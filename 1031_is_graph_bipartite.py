import collections


class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """

    def isBipartite(self, graph):
        # Write your code here
        if not graph:
            return True

        RED, UNK, BLUE = 1, 0, -1
        queue = collections.deque([])
        color_map = [0] * len(graph)

        for i in range(len(graph)):
            if color_map[i] != UNK:
                continue #has been colored
            color_map[i] = RED
            queue.append(i)
            while queue:
                node = queue.popleft()
                for next_node in graph[node]:
                    if color_map[next_node] == UNK:
                        color_map[next_node] = - color_map[node]
                        queue.append(next_node)
                    elif color_map[next_node] == color_map[node]:
                        return False

        return True