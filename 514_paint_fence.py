class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        if n< 3:
            return 0
        records = [0] * n
        records[0], records[1] = k, k*k

        for i in range(2, n):
            # if ith color == i-1th color
            records[i] += records[i-2]*(k-1)
            # if ith color != i-1th color
            records[i] += records[i-1]*(k-1)

        return records[-1]

if __name__ == '__main__':
    s = Solution()
    n = 3
    k = 2
    print(s.numWays(n, k))