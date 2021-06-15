class Solution:
    """
    @param s: the given string s
    @param t: the given string t
    @return: check if s is subsequence of t
    """

    def isSubsequence(self, s, t):
        # Write your code here
        if not t and not s:
            return True
        if not t:
            return False

        i_t = 0
        for i_s in range(len(s)):
            char_s = s[i_s]
            i_t = self.find_same(t, char_s, i_t)
            if i_t is None:
                return False
            else:
                i_t += 1
        return True

    def find_same(self, t, char, start):
        #print(char, start)
        for i in range(start, len(t)):
            if char == t[i]:
                return i
        return None

if __name__ == '__main__':
    solution = Solution()
    s = 'aaaaaa'
    t = 'bbaaaa'
    print(solution.isSubsequence(s, t))