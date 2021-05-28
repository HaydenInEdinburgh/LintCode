REVERSE_KEYBOARD = {
    "a": "2", "b": "2", "c": "2",
    "d": "3", "e": "3", "f": "3",
    "g": "4", "h": "4", "i": "4",
    "j": "5", "k": "5", "l": "5",
    "m": "6", "n": "6", "o": "6",
    "p": "7", "q": "7", "r": "7", "s": "7",
    "t": "8", "u": "8", "v": "8",
    "w": "9", "x": "9", "y": "9", "z": "9",
}
class TrieNode:
    def __init__(self):
        self.word_count = 0
        self.children = {}

    def add(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_count += 1

class Solution:
    """
    @param queries: the queries
    @param dict: the words
    @return: return the queries' answer
    """
    def letterCombinationsII(self, queries, dict):
        root = TrieNode()
        for word in dict:
            digit_word = ''.join([REVERSE_KEYBOARD[char] for char in word])
            root.add(digit_word)

        res = []
        for query in queries:
            node = root
            for digit in query:
                if digit not in node.children:
                    node = None
                    break
                node = node.children[digit]
            res.append(node.word_count if node else 0)
        return res
if __name__ == '__main__':
    query = ["2", "3", "4"]
    dict = ["a", "abc", "de", "fg"]
    s = Solution()
    print(s.letterCombinationsII(query, dict))