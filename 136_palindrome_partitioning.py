class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        if len(s) <= 1:
            return [[s]]

        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, start, path, res):
        if start >= len(s):
            res.append(path[:])
            return

        for end in range(start, len(s)):
            word = s[start:end+1]
            #print(start, end, word)
            if not self.isPalindrome(word):
                continue
            path.append(word)
            self.dfs(s, end+1, path, res)
            path.pop()

    def isPalindrome(self, word):
        return word == word[::-1]


if __name__ == '__main__':
    s = Solution()
    input = "a"
    print(s.partition(input))