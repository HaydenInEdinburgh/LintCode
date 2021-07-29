class TrieNode:
    def __init__(self, char = None):
        self.char = char
        self.child = {}
        self.isword = False
        self.word_list = []

class Trie:
    def __init__(self, words):
        self.dummy = TrieNode()
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        node = self.dummy
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode(c)
            node = node.child[c]
            node.word_list.append(word)

        node.isword = True

    def find(self, word):
        node = self.dummy
        for c in word:
            if c not in node.child:
                return False
            node = node.child[c]

        return node

    def get_words_by_prefix(self, prefix):
        node = self.find(prefix)
        if not node:
            return []
        return node.word_list


class Solution:
    """
    @param words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        trie = Trie(words)

        squares = []
        for word in words:
            self.search(trie, [word], squares)

        return squares

    def search(self, trie, square, squares):#dfs
        n = len(square[0])
        cur_idx = len(square)
        if cur_idx == n:
            squares.append(square[:])
            return

        #pruning 2
        for r_idx in range(cur_idx, n):
            prefix = ''.join([square[i][r_idx] for i in range(cur_idx)])
            if trie.find(prefix) is None:
                return

        prefix = ''.join([square[i][cur_idx] for i in range(cur_idx)])
        for word in trie.get_words_by_prefix(prefix):
            square.append(word)
            self.search(trie, square, squares)
            square.pop()