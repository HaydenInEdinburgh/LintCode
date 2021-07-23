import sys


class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        if not target or not source:
            return ""

        t_cnt = self.get_cnt(target)
        s_cnt = {}
        l, r, valid = 0, 0, 0
        min_length, res = sys.maxsize, ""
        while r < len(source):
            char = source[r]
            s_cnt[char] = s_cnt.get(char, 0) + 1
            if char in t_cnt and t_cnt[char] == s_cnt[char]:
                valid += 1
            while valid == len(t_cnt):
                # update
                if r - l + 1 < min_length:
                    res = source[l:r+1]
                    min_length = min(min_length, r-l+1)
                s_cnt[source[l]] -= 1
                if source[l] in t_cnt and s_cnt[source[l]] < t_cnt[source[l]]:
                    valid -= 1
                l += 1
            r += 1

        return res

    def get_cnt(self, word):
        cnt = {}
        for char in word:
            cnt[char] = cnt.get(char, 0) +1

        return cnt



if __name__ == '__main__':
    s= Solution()
    source = "adobec"
    target = "abc"
    print(s.minWindow(source, target))