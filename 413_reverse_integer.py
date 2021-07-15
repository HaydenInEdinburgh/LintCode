class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        # write your code here
        MAXINT = (1 << 32) - 1
        sign = 1 if n >= 0 else -1
        n_str = str(n) if n >= 0 else str(n)[1:]

        if int(n_str[::-1]) > MAXINT:
            return 0
        return sign * int(n_str[::-1])