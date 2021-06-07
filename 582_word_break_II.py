# class Solution:
#       hit memory limit ---> NOT WORKING
#     """
#     @param: s: A string
#     @param: wordDict: A set of words.
#     @return: All possible sentences.
#     """
#     def wordBreak(self, s, wordDict):
#         # write your code here
#         if not s or not wordDict:
#             return []
#
#         n = len(s)
#         dp = {i: [] for i in range(n+1)}
#         max_length = max([len(w) for w in wordDict])
#
#         for i in range(1, n+1):
#             for j in range(max(i-max_length, 0), i):
#                 if s[j:i] in wordDict:
#                     #print(s[j:i])
#                     if j == 0:
#                         dp[i].append([s[:i]])
#                     elif len(dp[j]) != 0 :
#                         self.add_comb(dp, s, i, j)
#         #print(dp)
#         return [' '.join(comb) for comb in dp[n]]
#
#     def add_comb(self, dp, s, i, j):
#         new_word = s[j:i]
#         for comb in dp[j]:
#             dp[i].append(comb + [new_word])


class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        if not s or not wordDict:
            return []

        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return []

        partitions = []
        if s in wordDict:
            partitions.append(s)

        for i in range(1, len(s)):
            word = s[:i]
            if word not in wordDict:
                continue
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for sub in sub_partitions:
                partitions.append(word + " " + sub)

        memo[s] = partitions
        return partitions

if __name__ == '__main__':
    sl = Solution()
    s = "lintcode"
    dict = {"de", "ding", "co", "code", "lint"}
    print(sl.wordBreak(s, dict))