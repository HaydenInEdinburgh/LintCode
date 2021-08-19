import sys


class Solution:
    """
    @param S: A source string
    @param T: A target string
    @return: The String contains the smallest substring of all T letters.
    """

    def minWindowII(self, S, T):
        # Write your code here
        if not S or not T:
            return ''

        S = S +S
        #print(S)
        t_cnt = self.get_count(T)

        complete = 0
        s_cnt = {}
        l, r = 0, 0
        res, length = None, sys.maxsize
        while r < len(S):
            char = S[r]
            s_cnt[char] = s_cnt.get(char, 0) +1
            if char in t_cnt and s_cnt[char] == t_cnt[char]:
                complete += 1
            while complete == len(t_cnt):
                if r-l+1 < length:
                    length, res = r-l+1, S[l:r+1]
                    print(S[l:r+1])
                s_cnt[S[l]] -= 1
                if S[l] in t_cnt and s_cnt[S[l]] < t_cnt[S[l]]:
                    complete -= 1
                l += 1
            r += 1
        return res

    def get_count(self, word):
        cnt = {}
        for c in word:
            cnt[c] = cnt.get(c, 0) + 1
        return cnt

if __name__ == '__main__':
    s = Solution()
    S = "ADOBECODEBANC"
    T = "DAOC"
    print(s.minWindowII(S, T))