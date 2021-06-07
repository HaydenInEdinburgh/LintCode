import sys


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        maximums = self.get_maximums_after(prices)
        print(maximums)
        max_profit = -0
        for i in range(len(prices)-1):
            profit = maximums[i+1] - prices[i]
            max_profit = max(max_profit, profit)

        return max_profit


    def get_maximums_after(self, prices):
        maximum = - sys.maxsize
        results = []
        for n in reversed(prices):
            maximum = max(maximum, n)
            results.append(maximum)

        return results[::-1]

if __name__ == '__main__':
    s = Solution()
    prices = [5, 4, 3, 2, 1]
    print(s.maxProfit(prices))