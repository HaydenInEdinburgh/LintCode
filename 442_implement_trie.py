class Node:
    def __init__(self, char=None):
        self.char = char
        self.next = {}
        self.is_word = False

class Trie:

    def __init__(self):

    # do intialization if necessary
        self.dummy = Node()
    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word):
    # write your code here
        node = self.dummy
        for c in word:
            if c not in node.next:
                node.next[c] = Node(c)
            node = node.next[c]
        node.is_word = True

    """ 
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word):
        node = self.find(word)
    # write your code here
        return  node is not None and node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        # write your code here
        return self.find(prefix) is not None

    def find(self, word):
        node = self.dummy
        for c in word:
            if c not in node.next:
                return None
            node = node.next[c]

        return node

if __name__ == '__main__':
    s = Trie()
    s.insert('aaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaa')
    print(s.startsWith('aaaa'))