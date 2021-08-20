class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] >0:
                profit += prices[i] - prices[i-1]

        return profit

if __name__ == '__main__':
    s = Solution()
    prices = [1, 2, 4]
    print(s.maxProfit(prices))