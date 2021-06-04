class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        if not pattern and not teststr:
            return True
        if not pattern or not teststr:
            return False

        words = teststr.split(' ')
        pattern_to_word = {}
        word_to_pattern = {}
        for i in range(len(pattern)):
            p, w = pattern[i], words[i]
            if p in pattern_to_word:
                if pattern_to_word[p] == w:
                    continue
                else:
                    return False
            else:
                if w in word_to_pattern and word_to_pattern[w] != p:
                    return False
                pattern_to_word[p] = w
                word_to_pattern[w] = p
        return True

if __name__ == '__main__':
    s = Solution()
    word = "a dog dog a"
    pattern = "abba"
    print(s.wordPattern(pattern, word))