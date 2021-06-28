class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: return an integer
    """
    #Recursion
    
    def longestSubstring(self, s, k):
        # write your code here
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(substring, k) for substring in s.split(c))
        return len(s)