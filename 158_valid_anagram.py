class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        s_ord = [0] * 256
        for char in s:
            s_ord[ord(char)] += 1

        for char in t:
            s_ord[ord(char)] -= 1
            if s_ord[ord(char)] < 0:
                return False

        return sum(s_ord) == 0