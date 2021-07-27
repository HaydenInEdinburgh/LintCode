class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        self.child = {}
        for i in range(1, n+1):
            self.father[i] = i
            self.child[i] = 1
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.child[root_b] += self.child[root_a]
    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        res = self.child[self.find(a)]
        return res

    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node

if __name__ == '__main__':
    c = ConnectingGraph2(5)
    print(c.query(1))
    c.connect(1, 2)
    print(c.query(1))
    c.connect(2, 4)
    print(c.query(1))
    # connect(1, 4)
    # query(1)