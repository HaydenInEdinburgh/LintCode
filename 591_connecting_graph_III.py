class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """

    def __init__(self, n):
    # initialize your data structure here.
        self.father = {i: i for i in range(1, n+1)}
        self.components = n

    def connect(self, a, b):
        # write your code here
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.components -= 1

    """
    @return: An integer
    """

    def query(self):
        # write your code here
        return self.components

    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node
