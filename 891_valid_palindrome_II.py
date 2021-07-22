class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        if len(s) <= 1: return True

        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                omit_l = s[l+1:r+1]
                omit_r = s[l:r]
                return omit_l[::-1] == omit_l or omit_r == omit_r[::-1]

        return True

if __name__ == '__main__':
    string = 'aabcaba'
    s = Solution()
    print(s.validPalindrome(string))