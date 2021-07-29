class TrieNode:

    def __init__(self):
        self.child = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        # write your code here
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.is_word = True


    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        if not word: return False
        node = self.root
        return self.find(node, word, 0)

    def find(self, node, word, index):
        if not node:
            return False

        if index == len(word):
            return node.is_word

        c = word[index]
        if c != '.':
            return self.find(node.child.get(c), word, index+1)
        else:
            for child in node.child:
                if self.find(node.child[child], word, index+1):
                    return True

        return False

if __name__ == '__main__':
    s = WordDictionary()
    s.addWord('bad')