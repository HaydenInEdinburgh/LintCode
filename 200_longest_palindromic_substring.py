class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    # Time => O(n^2)
    def longestPalindrome(self, s):
        # write your code here
        if len(s) <= 1: return s

        maxRes = (0, 0)
        for i in range(len(s)):
            maxRes = max(maxRes, self.extend(s, i, i))
            maxRes = max(maxRes, self.extend(s, i, i+1))

        return s[maxRes[1]: maxRes[1] + maxRes[0]]

    def extend(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right-left-1, left+1