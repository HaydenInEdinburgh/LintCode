class Solution:
    """
    @param S: the string
    @return: return the number of “Balance” in the string
    """
    def find(self, S):
        # write your code here
        if not S:
            return 0
        left_prefix = self.get_prefix(S)
        right_prefix = self.get_prefix(S[1:][::-1])[::-1]

        res = 0
        print(left_prefix)
        print(right_prefix)
        for i in range(len(S)-1):
            if left_prefix[i] == right_prefix[i]:
                res += 1

        return res

    def get_prefix(self, S):
        n = len(S)
        char_set = set()
        left = []
        for i in range(n):
            char = S[i]
            char_set.add(char)
            left.append(len(char_set))

        return left


if __name__ == '__main__':
    s = Solution()
    S = 'aabcd'
    print(s.find(S))