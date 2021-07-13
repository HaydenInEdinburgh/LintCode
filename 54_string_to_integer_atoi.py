import sys


class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def atoi(self, s):
        # write your code here
        s = str.strip(s)
        if not s:
            return 0

        i = 0
        while s[i] == '0':
            i += 1
        sign = 1
        ret = 0
        MaxInt = (1 << 31) - 1
        if s[i] == '-':
            sign *= -1
            i += 1
        elif s[i] == '+':
            i += 1

        for j in range(i, len(s)):
            if s[j] < '0' or s[j] > '9':
                break
            ret = ret * 10 + int(s[j])
            if ret > sys.maxsize:
                break
        ret *= sign
        #print(ret, sign)
        if ret >= MaxInt:
            return MaxInt
        if ret < MaxInt * -1:
            return MaxInt * - 1 - 1
        return ret

if __name__ == '__main__':
    s = Solution()
    string = '10'
    print(s.atoi(string))