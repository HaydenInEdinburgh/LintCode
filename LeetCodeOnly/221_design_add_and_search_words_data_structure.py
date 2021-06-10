class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = False
        self.dummy = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.dummy
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    def search(self, word: str) -> bool:
        self.res = False
        node = self.dummy
        self.dfs(word, node)
        return self.res

    def dfs(self, word, node):
        if not word:
            if node.is_word:
                self.res = True
            return

        if word[0] == '.':
            for node in node.children.values():
                self.dfs(word[1:], node)
        else:
            if word[0] not in node.children:
                return
            node = node.children[word[0]]
            self.dfs(word[1:], node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)