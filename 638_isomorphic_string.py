class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False

        char_dict = {}
        assigned = set()
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            if char_s not in char_dict:
                if char_t in assigned:
                    return False
                char_dict[char_s] = char_t
                assigned.add(char_t)
            elif char_t != char_dict[char_s]:
                return False

        return True