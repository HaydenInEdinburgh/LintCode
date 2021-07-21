class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # Write your code here
        if not J:
            return 0

        S_cnt = {}
        for char in S:
            S_cnt[char] = S_cnt.get(char, 0) + 1
        res = 0
        for c in J:
            res += S_cnt.get(c, 0)

        return res