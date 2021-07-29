DIRECTION = [(1, 0), (-1, 0), (0, -1), (0, 1)]
class Solution_DFS:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words:
            return []

        prefix_set = self.get_prefix_set(words)
        word_set = set(words)

        res = set()
        for x in range(len(board)):
            for y in range(len(board[0])):
                visited = {(x, y)}
                self.search(board, x, y, board[x][y], visited, prefix_set, word_set, res)
        return list(res)

    def search(self, board, x, y, word, visited, prefix_set, word_set, res):
        if word not in prefix_set:
            return
        if word in word_set:
            res.add(word)

        for dx, dy in DIRECTION:
            nx, ny = x+dx, y+dy
            if not self.isValid(board, nx, ny):
                continue
            if (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            self.search(board, nx, ny, word + board[nx][ny], visited, prefix_set, word_set, res)
            visited.remove((nx, ny))


    def get_prefix_set(self, words):
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                if word[:i+1] not in prefix_set:
                    prefix_set.add(word[:i+1])
        return prefix_set

    def isValid(self, board, x, y):
        return 0<= x< len(board) and 0<= y< len(board[0])


class TrieNode:
    def __init__(self, word = None):
        self.word = word
        self.child = {}
        self.isword = False

class Trie:
    def __init__(self):
        self.dummy = TrieNode()

    def add_word(self, word):
        node = self.dummy
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.isword = True
        node.word = word

    def find(self, word):
        node = self.dummy
        for c in word:
            if c not in node.child:
                return None
            node = node.child[c]
        return node

class Solution_Trie:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        trie = Trie()
        for word in words:
            trie.add_word(word)

        results = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                self.search(trie.dummy.child.get(char), i, j, board, {(i, j)}, results)

        return list(results)

    def search(self, node, cur_x, cur_y, board, visited, results):
        if not node:
            return
        if node.isword:
            results.add(node.word)

        for dx, dy in DIRECTION:
            nx, ny = cur_x+dx, cur_y+dy
            if not self.valid(board, nx, ny):
                continue
            if (nx, ny) in visited:
                continue

            visited.add((nx, ny))
            self.search(node.child.get(board[nx][ny]), nx, ny, board, visited, results)
            visited.remove((nx, ny))


    def valid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])


if __name__ == '__main__':
    board = ["b","a","b","b","a"]
    words = ["babbab","b","a","ba"]
    expected = ["a","b","ba"]
    print(Solution_Trie().wordSearchII(board, words))