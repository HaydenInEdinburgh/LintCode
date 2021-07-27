class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        # Write your code here
        if not s:
            return True

        char_cnt = {}
        res = []
        for char in s:
            char_cnt[char] = char_cnt.get(char, 0) +1
            r = self.check_arr(char_cnt)
            res.append(r)
        return res

    def check_arr(self, char_cnt):
        odd = 0
        for c, val in char_cnt.items():
            if val % 2 != 0:
                odd += 1
        return int(odd <= 1)
if __name__ == '__main__':
    s = Solution()
    string = ['a','a','a','a','a']
    print(s.getStream(string))