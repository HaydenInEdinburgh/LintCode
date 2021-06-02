import collections


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return

        nodes = self.get_nodes(node)
        mapping = {n: UndirectedGraphNode(n.label) for n in nodes}

        for n in nodes:
            new_node = mapping[n]
            for neighbor in n.neighbors:
                new_node.neighbors.append(mapping[neighbor])

        return mapping[node]

    def get_nodes(self, root):
        queue = collections.deque([root])
        nodes = {root}
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor in nodes:
                    continue
                queue.append(neighbor)
                nodes.add(neighbor)

        return nodes
