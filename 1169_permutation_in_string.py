class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    # Sliding Window
    def checkInclusion(self, s1, s2):
        # write your code here
        if len(s1) > len(s2):
            return False
        n, m = len(s1), len(s2)
        target_set = self.cal_char(s1)
        source_set = self.cal_char(s2[:n])
        # dictionary can be compared
        if target_set == source_set:
            return True

        for win_start in range(1, m-n+1):
            win_end = win_start + n - 1
            source_set[s2[win_end]] = source_set.get(s2[win_end], 0) + 1
            source_set[s2[win_start -1]] -= 1

            if source_set[s2[win_start -1]] == 0:
                del source_set[s2[win_start -1]]

            if source_set == target_set:
                return True

        return False

    def cal_char(self, s):
        dict = {}
        for char in s:
            dict[char] = dict.get(char, 0) + 1
        return dict