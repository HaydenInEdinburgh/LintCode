class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if len(s) <= 1:
            return len(s)

        right = 0
        char = set([])
        longest = 0

        for left in range(len(s)):
            while right < len(s) and s[right] not in char:
                char.add(s[right])
                right += 1
            longest = max(longest, right - left)
            char.remove(s[left])#左指针移动

        return longest