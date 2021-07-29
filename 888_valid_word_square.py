class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        n = len(words)
        for i in range(n):
            row = words[i]
            col = ''.join([w[i] for w in words])
            if row != col:
                return False

        return True