class Solution_MEMO:
    # Memo Search hits memory limit -> not work
    """
	@param s: A string
	@param wordSet: A dictionary of words dict
	@return: A boolean
	"""

    def wordBreak(self, s, wordSet):
        # write your code here
        if not s:
            return True
        max_length = self.get_max_length(wordSet)
        return self.dfs(s, max_length, wordSet, {})

    def dfs(self, s, max_length, wordSet, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return True
        for i in range(1, min(len(s), max_length) + 1):
            if s[:i] not in wordSet:
                continue
            canBreak = self.dfs(s[i:], max_length, wordSet, memo)
            if canBreak:
                memo[s] = True
                return True

        memo[s] = False
        return False

    def get_max_length(self, wordSet):
        max_length = 0
        for word in wordSet:
            max_length = max(max_length, len(word))

        return max_length


class Solution_DFS:
    # Time limit was hit ---> not working
    def wordBreak(self, s, wordSet):
        if not s:
            return True
        return self.dfs(s, 0, wordSet)

    def dfs(self, s, start, wordSet):
        if start == len(s):
            return True

        for word in wordSet:
            if len(word) + start > len(s):
                continue
            if s[start: start + len(word)] == word:
                if self.dfs(s, start + len(word), wordSet):
                    return True

        return False


class Solution:
    def wordBreak(self, s, wordSet):
        if not s:
            return True
        if not dict:
            return False

        n = len(s)
        dp = [False] * (n + 1)
        maxLen = max([len(w) for w in wordSet])
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(max(i - maxLen, 0), i):
                if not dp[j]:
                    continue
                if s[j: i] in wordSet:
                    dp[i] = True
                    break

        return dp[-1]


class Solution:
    """
	@param s: A string
	@param wordSet: A dictionary of words dict
	@return: A boolean
	"""

    def wordBreak(self, s, wordSet):
        # write your code here
        if not s:
            return True

        dp = [False] * (len(s) + 1)
        dp[0] = True

        maxLen = max([len(w) for w in wordSet])

        for i in range(1, len(s) + 1):
            for j in range(max(i - maxLen, 0), i):
                if not dp[j]:
                    continue
                if s[j:i] not in wordSet:
                    continue
                dp[i] = True

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    string = "a"
    wordSet = set(["a"])
    print(s.wordBreak(string, wordSet))
