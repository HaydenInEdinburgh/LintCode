class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        # write your code here
        if not num: return [0]
        dp = [0]
        for i in range(1, num+1):
            dp.append(dp[i>>1] + i%2)

        return dp

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(5))


