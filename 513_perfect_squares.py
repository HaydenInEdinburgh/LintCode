import sys


class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        if not n: return 0
        nums = self.get_square_nums(n)
        self.res = sys.maxsize

        self.dfs(0, 0, n, nums)
        return self.res

    def dfs(self, cur_sum, length, n, nums):
        #exit
        if length > self.res or cur_sum > n:
            return

        if cur_sum == n:
            self.res = min(self.res, length)
            return

        for digit in nums:
            # print(cur_sum +digit)
            self.dfs(cur_sum+digit, length+1, n, nums)



    def get_square_nums(self, n):
        nums = []
        for i in range(1, n+1):
            square = i **2
            if square > n:
                break
            nums.append(square)

        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))