import sys
class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        if not amount:
            return 0
        coins = set(coins)
        dp = [0] * (amount+1)
        # init
        for c in coins:
            if c < amount:
                dp[c] = 1

        for i in range(1, amount+1):
            #print(dp)
            if dp[i] != 0:
                continue
            minimum = self.find_min(dp, i, coins)
            if minimum != -1:
                dp[i] = minimum

        if not dp[-1]:
            return -1
        return dp[-1]

    def find_min(self, dp, i, coins):
        minimum = sys.maxsize
        for c in coins:
            if i < c or c == 0:
                continue
            if i > c and dp[i-c] == 0:
                continue
            minimum = min(minimum, dp[i-c])
        if minimum == sys.maxsize:
            return -1
        return minimum + 1

if __name__ == '__main__':
    s = Solution()
    coins = [1]
    amount = 1
    print(s.coinChange(coins, amount))