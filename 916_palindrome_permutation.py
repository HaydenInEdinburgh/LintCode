class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        if len(s) <= 1:
            return True

        char_cnt = {}
        for char in s:
            char_cnt[char] = char_cnt.get(char, 0) + 1

        res = 0
        for _, cnt in char_cnt.items():
            res += (cnt %2)

        return res <= 1