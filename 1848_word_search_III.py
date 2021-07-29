DIRECTION = [(1, 0), (-1, 0), (0, -1), (0, 1)]
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

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchIII(self, board, words):
        # write your code here
        trie = Trie()
        for word in words:
            trie.add_word(word)

        return self.dfs(board, trie, set(), 0, -1)

    def dfs(self, board, trie, visited, start_i, start_j):
        m, n = len(board), len(board[0])
        cnt = 0
        for i in range(start_i, m):
            _j = start_j +1 if i == start_i else 0
            for j in range(_j, n):
                if (i, j) in visited:
                    continue
                c = board[i][j]
                if c not in trie.dummy.child:
                    continue
                visited.add((i, j))
                cnt = max(cnt, self.search(board, i, j, trie, trie.dummy.child[c], visited, i, j))
                visited.remove((i, j))
        return cnt


    def search(self, board, x, y, trie, node, visited, start_i, start_j):
        m, n = len(board), len(board[0])
        cnt = 0

        if node.isword:
            node.isword = False
            cnt = self.dfs(board, trie, visited, start_i, start_j) + 1
            node.isword = True

        for dx, dy in DIRECTION:
            nx, ny = x+dx, y+dy
            if not self.valid(board, nx, ny):
                continue
            if (nx, ny) in visited:
                continue
            c = board[nx][ny]
            if c not in node.child:
                continue
            visited.add((nx, ny))
            cnt = max(cnt, self.search(board, nx, ny, trie, node.child[c], visited, start_i, start_j))
            visited.remove((nx, ny))

        return cnt

    def valid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
