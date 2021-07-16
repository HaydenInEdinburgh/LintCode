class Solution:
    """
    @param ransomNote: a string
    @param magazine: a string
    @return: whether the ransom note can be constructed from the magazines
    """
    def canConstruct(self, ransomNote, magazine):
        # Write your code here
        if not ransomNote:
            return True

        mgz_cnt = self.get_cnt(magazine)
        for i, c in enumerate(ransomNote):
            if c not in mgz_cnt or mgz_cnt[c] == 0:
                return False
            mgz_cnt[c] -= 1

        return True

    def get_cnt(self, word):
        cnt = {}
        for char in word:
            cnt[char] = cnt.get(char, 0) + 1

        return cnt