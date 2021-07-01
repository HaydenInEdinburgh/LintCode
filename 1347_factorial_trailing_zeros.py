class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def trailingZeroes(self, n):
        # write your code here
        if not n:
            return 0
        return self.trailingZeroes(n//5) + n//5