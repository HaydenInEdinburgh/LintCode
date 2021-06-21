class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            s_index = i - 1
            print(s_index, s[s_index])
            if i == 1:
                if s[s_index] != '0':
                    dp[i] = 1
                    continue
                else:
                    return 0
            tmp = 0
            if 0 < int(s[s_index]) <= 26: #can be single decoded
                tmp += dp[i-1]
            if 0 < int(s[s_index-1: s_index+1]) <= 26 and s[s_index-1] != '0':
                tmp += dp[i-2]
            dp[i] = tmp

        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    string = "06"
    print(s.numDecodings(string))