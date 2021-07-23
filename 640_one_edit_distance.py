class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        m, n = len(s), len(t)
        dif = abs(m - n)
        if s == t or dif >1:
            return False
        if m < n:
            s, t = t, s
            m, n = n, m

        if dif:
            for i in range(n):
                if s[i] != t[i]:
                    return s[i+1:] == t[i:]

            return True
        else:
            char_dif = 0
            for i in range(n):
                if s[i] != t[i]:
                    char_dif += 1

            return char_dif == 1

if __name__ == '__main__':
    s = Solution()
