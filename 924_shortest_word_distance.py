class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        if not words:
            return -1

        last_word1, last_word2 = None, None
        min_dis = len(words)

        for i in range(len(words)):
            word = words[i]
            if word == word1:
                if last_word2 != None:
                    min_dis = min(i - last_word2, min_dis)
                last_word1 = i
            if word == word2:
                if last_word1 != None:
                    min_dis = min(min_dis, i - last_word1)
                last_word2 = i

        return min_dis


if __name__ == '__main__':
    s = Solution()
    words = ["a","b"]
    word1 = "a"
    word2 = "b"
    print(s.shortestDistance(words, word1, word2))