class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        if not pattern or not str:
            return False

        p_to_word = {}
        used = set()
        return self.dfs(pattern, 0, str, 0, p_to_word, used)

    def dfs(self, pattern, i, source, j, p_to_word, used):
        if i == len(pattern):
            return j == len(source)

        p = pattern[i]
        if p in p_to_word:
            word = p_to_word[p]
            if not source[j:].startswith(word):
                return False
            return self.dfs(pattern, i+1, source, j+len(word), p_to_word, used)

        for index in range(j, len(source)):
            word = source[j: index+1]
            if word in used:
                continue
            used.add(word)
            p_to_word[p] = word
            if self.dfs(pattern, i+1, source, index+1, p_to_word, used):
                return True
            del p_to_word[p]
            used.remove(word)

        return False

if __name__ == '__main__':
    s = Solution()
    pattern = "d"
    str = "ef"
    print(s.wordPatternMatch(pattern, str))