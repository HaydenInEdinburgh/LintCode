class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        # Write your code here
        if not s or not dict:
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        max_length = max([len(w) for w in dict])
        dict = set([word.lower() for word in dict])
        #print(dict)
        for i in range(1, n+1):
            cnt = 0
            for j in range(max(i-max_length, 0), i):
                #print(s[j:i], s[j:i] in dict)
                if s[j:i].lower() in dict and dp[j]:
                    cnt += dp[j]
            dp[i] = cnt

        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    string = "Catmat"
    dict = ["Cat", "mat", "Ca", "tm", "at", "C", "Dog", "og", "Do"]
    print(s.wordBreak3(string, dict))
