class UnionFind:
    def __init__(self, books):
        self.father = {b: b for b in books}
        self.group = {b: {b} for b in books}

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_b] = root_a
            self.group[root_a].update(self.group[root_b])

    def find(self, book):
        path = []
        while book != self.father[book]:
            path.append(book)
            book = self.father[book]

        for b in path:
            self.father[b] = book

        return book
class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        # Write your code here
        if not ListA or not ListB:
            return None

        edges = [[ListA[i], ListB[i]] for i in range(len(ListA))]
        books = set(ListA + ListB)

        uf = UnionFind(books)
        res, maxLen = None, 0
        for book_a, book_b in edges:
            uf.union(book_a, book_b)
            root_a = uf.find(book_a)
            if len(uf.group[root_a]) > maxLen:
                res = uf.group[root_a]
                maxLen = len(uf.group[root_a])

        return list(res)


if __name__ == '__main__':
    s = Solution()
    A = ["a","b","d","e","f"]
    B = ["b","c","e","g","g"]
    print(s.maximumAssociationSet(A, B))