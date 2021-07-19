class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        # write your code here
        print(1 >> 1 ^ 1)
        return  [i >> 1 ^ i for i in range(2 ** n)]

if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(2))