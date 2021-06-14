class Solution:
    """
    @param S: a string
    @return: return a string
    """
    def reorganizeString(self, S):
        # write your code here
        if not S:
            return S
        chars = list(S)

        char_cnt = {}
        for c in chars:
            char_cnt[c] = char_cnt.get(c, 0) + 1

        max_freq = max(char_cnt.values())
        if max_freq > (len(S) +1)//2:
            return ""

        buckets = [[] for _ in range(max_freq)]
        begin = 0
        for char, cnt in sorted(char_cnt.items(), key=lambda x: -x[1]):
            print(char, cnt)
            for i in range(cnt):
                buckets[(i+begin) % max_freq].append(char)
            begin += cnt
        print(buckets)
        return ''.join([''.join(x) for x in buckets])

if __name__ == '__main__':
    s = Solution()
    input = "blflxll"
    print(s.reorganizeString(input))